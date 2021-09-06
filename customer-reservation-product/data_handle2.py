import time

import requests
import json
from collections import Counter

environments = 'Gross_Pricing'
year_str = '2020'
year_month_str = '2020-12'
year_month_end_day_str = '2020-12-31'


if __name__ == '__main__':
    with open('../Gross_Pricing_all_reservations_'+year_str+'.json', 'r') as reservation_f:
        reservation_list = json.load(reservation_f)
    print('total reservation = ', len(reservation_list))

    with open('data/Gross_Pricing_room_resource_categories.json', 'r') as categories_f:
        categories_list = json.load(categories_f)
    print('total categories = ', len(categories_list))

    with open('data/Gross_Pricing_reservation_'+year_month_str.replace('-', '_')+'.json', 'r') as need_reservation_f:
        need_reservation_list = json.load(need_reservation_f)
    print('need reservation = ', len(need_reservation_list))

    vaild_category_ids = []
    for category in categories_list:
        vaild_category_ids.append(category['Id'])
    pass

    reservation_new_need = []
    count_reservation_category_ids = []
    for reservation in reservation_list:
        if reservation['StartUtc'][:7] == year_month_str:
            reservation_new_need.append(reservation)
            count_reservation_category_ids.append(reservation['RequestedCategoryId'])
        pass
    pass
    print('total reservation new need = ', len(reservation_new_need))

    count_reservation_category = Counter(count_reservation_category_ids)
    print(count_reservation_category)

    for reservation in reservation_new_need:
        reservation['countInMonth'] = count_reservation_category[reservation['RequestedCategoryId']]
        # 看是否在need_reservation_list
        for need_reservation in need_reservation_list:
            if reservation['Id'] == need_reservation['reservationId']:
                reservation['rates'] = need_reservation['rates']
                reservation['Currency'] = need_reservation['Currency']
                break
            pass
        pass

    with open('data/'+environments+"_reservation_"+year_month_str.replace('-', '_')+"new2.json", "w+") as json_file:
        json_file.write(json.dumps(reservation_new_need, indent=4))
    pass

