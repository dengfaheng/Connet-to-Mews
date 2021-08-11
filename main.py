import requests
import json


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    url = 'https://api.mews-demo.com/api/connector/v1/reservations/getAll'
    data = {
                "ClientToken": "E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
                "AccessToken": "C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
                "Client": "Sample Client 1.0.0",
                "StartUtc": "2016-01-01T00:00:00Z",
                "EndUtc": "2016-01-07T00:00:00Z",
                "ServiceIds": [
                    "bd26d8db-86da-4f96-9efc-e5a4654a4a94"
                ],
                "RateIds": [
                    "ed4b660b-19d0-434b-9360-a4de2ea42eda"
                ],
                # "States": [
                #     "Started"
                # ],
                "Extent": {
                    "Reservations": True,
                    "ReservationGroups": False,
                    "Customers": False,
                    "Products": True
                }
            }

    url2 = 'https://api.mews-demo.com/api/connector/v1/resources/getAll'
    data2 = {
        "ClientToken": "E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
        "AccessToken": "C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
        "Client": "Sample Client 1.0.0",
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

    res = requests.post(url=url, data=json.dumps(data))
    res = json.loads(res.text)

    print(len(res['Reservations']))

    for reservation in res['Reservations']:
        print(reservation)

    res2 = requests.post(url=url2, data=json.dumps(data2))
    res2 = json.loads(res2.text)

    # with open("resource_categories_sample.json", "w+") as json_file:
    #     json_file.write(json.dumps(res2, indent=4))

    # print(res2)
    #
    # for reservation in res['Reservations']:
    #     pass
    #     print(reservation)



