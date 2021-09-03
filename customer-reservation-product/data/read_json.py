import json

with open('Gross_Pricing_customers_2020_12.json', 'r') as json_f:
    json_data = json.load(json_f)
print('total customers = ', len(json_data))