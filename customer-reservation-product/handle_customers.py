import time

import requests
import json

with open('data/Gross_Pricing_customers_2020_12.json', 'r') as customers_f:
    customers_list = json.load(customers_f)
print('total customers = ', len(customers_list))

customers_dict = dict()
for customer in customers_list:
    customers_dict[customer['Id']] = customer
pass

with open('data/Gross_Pricing_customers_2020_12.json', "w+") as json_file:
    json_file.write(json.dumps(customers_dict, indent=4))
pass
