import time

import requests
import json
from collections import Counter

environments = 'Gross_Pricing'
year_str = '2020'
year_month_str = '2020-12'
year_month_end_day_str = '2020-12-31'

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    with open('../Gross_Pricing_all_reservations_'+year_str+'.json', 'r') as reservation_f:
        reservation_list = json.load(reservation_f)
    print('total reservation = ', len(reservation_list))

    with open('data/Gross_Pricing_room_resource_categories.json', 'r') as categories_f:
        categories_list = json.load(categories_f)
    print('total categories = ', len(categories_list))

    vaild_category_ids = []
    for category in categories_list:
        vaild_category_ids.append(category['Id'])
    pass

    reservation_resource_category_ids = []
    count_reservation_category_ids = []
    for reservation in reservation_list:
        if reservation['StartUtc'][:7] == year_month_str:
            if reservation['RequestedCategoryId'] not in vaild_category_ids:
                continue
            pass
            reservation_resource_category_ids.append([reservation['RequestedCategoryId'], reservation['RateId'],
                                                      reservation['CustomerId'], reservation['Id']])
            count_reservation_category_ids.append(reservation['RequestedCategoryId'])
            # print(reservation_resource_category_ids[-1])
        pass
    pass
    print('total resource_category = ', len(reservation_resource_category_ids))

    known_rates = dict()
    need_products = []

    count_reservation_category = Counter(count_reservation_category_ids)
    print(count_reservation_category)


    for reservation_category in reservation_resource_category_ids:
        if reservation_category[1] not in known_rates.keys():
            # 请求该rate，并存储在字典中
            rate_url = 'https://api.mews-demo.com/api/connector/v1/rates/getPricing'
            rate_request_data = {
                "ClientToken": "E916C341431C4D28A866AD200152DBD3-A046EB5583FFBE94DE1172237763712",
                "AccessToken": "CC150C355D6A4048A220AD20015483AB-B6D09C0C84B09538077CB8FFBB907B4",
                "Client": "Sample Client 1.0.0",
                "RateId": reservation_category[1],
                "StartUtc": year_month_str+"-01T00:00:00Z",
                "EndUtc": year_month_end_day_str+"T00:00:00Z"
            }
            rate_res = requests.post(url=rate_url, data=json.dumps(rate_request_data))
            rate_res = json.loads(rate_res.text)
            if 'CategoryPrices' not in rate_res.keys():
                continue
            known_rates[reservation_category[1]] = rate_res
            print(rate_res)
        pass

        this_category_prices = []
        for category_rate in known_rates[reservation_category[1]]['CategoryPrices']:
            if category_rate['CategoryId'] == reservation_category[0]:
                this_category_prices = category_rate['Prices']
                break
            pass
        pass

        need_product = {
            "reservationId": reservation_category[3],
            "CustomerId": reservation_category[2],
            "CategoryId": reservation_category[0],
            "rates": this_category_prices,
            "Currency": known_rates[reservation_category[1]]['Currency'],
            "countInMonth": count_reservation_category[reservation_category[0]]
        }

        need_products.append(need_product)

        time.sleep(1)
    pass

    with open('data/'+environments+"_reservation_"+year_month_str.replace('-', '_')+".json", "w+") as json_file:
        json_file.write(json.dumps(need_products, indent=4))
    pass

