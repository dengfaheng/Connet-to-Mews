import requests
import json

environments = 'Gross_Pricing'
year_month_str = '2020-12'

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    with open("../Gross_Pricing_all_reservations_2020.json", 'r') as reservation_f:
        reservation_list = json.load(reservation_f)
    print(reservation_list[0])

    customer_ids = []
    for reservation in reservation_list:
        if reservation['StartUtc'][:7] == year_month_str:
            customer_ids.append(reservation['CustomerId'])
        pass
    pass
    print(len(customer_ids))

    post_data = {
                    "ClientToken": "E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
                    "AccessToken": "C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
                    "Client": "Sample Client 1.0.0",
                    "CustomerIds": customer_ids,
                    "Extent": {
                        "Customers": True,
                        "Documents": False,
                        "Addresses": False
                    }
                }
    connect_url = 'https://api.mews-demo.com/api/connector/v1/customers/getAll'
    resp = requests.post(url=connect_url, data=json.dumps(post_data))
    resp = json.loads(resp.text)

    with open('data/'+environments+"_customers_"+year_month_str.replace('-', '_')+".json", "w+") as json_file:
        json_file.write(json.dumps(resp['Customers'], indent=4))
    pass



