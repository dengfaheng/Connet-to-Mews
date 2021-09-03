import requests
import json

environments = 'Gross_Pricing'

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    post_data = {
                "ClientToken": 'E916C341431C4D28A866AD200152DBD3-A046EB5583FFBE94DE1172237763712',
                "AccessToken": 'CC150C355D6A4048A220AD20015483AB-B6D09C0C84B09538077CB8FFBB907B4',
                "Client": 'Sample Client 1.0.0',
                "Extent": {
                    "Resources": False,
                    "ResourceCategories": True,
                    "ResourceCategoryAssignments": False,
                    "ResourceCategoryImageAssignments": False,
                    "ResourceFeatures": False,
                    "ResourceFeatureAssignments": False,
                    "Inactive": False
                }
            }
    connect_url = 'https://api.mews-demo.com/api/connector/v1/resources/getAll'
    resp = requests.post(url=connect_url, data=json.dumps(post_data))
    resp = json.loads(resp.text)

    print(resp)

    room_list = []
    for category in resp['ResourceCategories']:
        if category['IsActive'] and category['Type'] == 'Room':
            room_list.append(category)
        pass
    pass

    with open('data/'+environments+"_room_resource_categories.json", "w+") as json_file:
        json_file.write(json.dumps(room_list, indent=4))
    pass




