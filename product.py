import requests
import json


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    url = 'https://api.mews-demo.com/api/connector/v1/products/getAll'
    data = {
                "ClientToken": "E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
                "AccessToken": "C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
                "Client": "Sample Client 1.0.0",
                "ServiceIds": [
                    "bd26d8db-86da-4f96-9efc-e5a4654a4a94"
                ]
            }

    res = requests.post(url=url, data=json.dumps(data))
    res = json.loads(res.text)

    for prod in res['Products']:
        print(prod['Name'])




