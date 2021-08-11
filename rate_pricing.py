import requests
import json


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    url = 'https://api.mews-demo.com/api/connector/v1/rates/getPricing'
    data = {
                "ClientToken": "E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D",
                "AccessToken": "C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D",
                "Client": "Sample Client 1.0.0",
                "RateId": "ed4b660b-19d0-434b-9360-a4de2ea42eda",
                "StartUtc": "2021-05-03T13:35:50Z",
                "EndUtc": "2021-05-05T08:00:00Z"
            }

    res = requests.post(url=url, data=json.dumps(data))
    res = json.loads(res.text)

    # print(res)
    with open("rate_pricing_sample.json", "w+") as json_file:
        json_file.write(json.dumps(res, indent=4))




