import requests
import json


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    url = 'https://api.mews-demo.com/api/connector/v1/services/getAll'
    data = {
                "ClientToken": "E916C341431C4D28A866AD200152DBD3-A046EB5583FFBE94DE1172237763712",
                "AccessToken": "1AEFA58C55E74D65BDC7AD2001564C12-66633E0B736F523379B9E5966165A55",
                "Client": "Sample Client 1.0.0"
            }

    res = requests.post(url=url, data=json.dumps(data))
    res = json.loads(res.text)

    for ser in res['Services']:
        print(ser['Name']+'->', ser['Id'])





