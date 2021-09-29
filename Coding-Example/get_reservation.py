import requests
import json


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    url = 'https://api.mews-demo.com/api/connector/v1/reservations/getAll'
    # Noting that we may use the `ServiceIds` in `data`.
    # `ServiceIds` denote the services provided by reservations.
    # There are many kinds of services, for example, "Meeting Room", "Breakfast", "Pxier Spa"...
    # Here we concern about the reservations with services "Stay".
    # So to query the reservations with services "Stay",
    # we need the `ServiceId` of service "Stay", that is, "bd26d8db-86da-4f96-9efc-e5a4654a4a94"
    data = {
            "ClientToken": "E916C341431C4D28A866AD200152DBD3-A046EB5583FFBE94DE1172237763712",
            "AccessToken": "CC150C355D6A4048A220AD20015483AB-B6D09C0C84B09538077CB8FFBB907B4",
            "Client": "Sample Client 1.0.0",
            "StartUtc": "2020-01-01T00:00:00Z",
            "EndUtc": "2020-01-07T00:00:00Z",
            "ServiceIds": [
                "bd26d8db-86da-4f96-9efc-e5a4654a4a94"
            ],
            "Extent": {
                "Reservations": True,
                "ReservationGroups": False,
                "Customers": False
            }
        }

    res = requests.post(url=url, data=json.dumps(data))
    res = json.loads(res.text)
    # print(res)

    if res['Reservations'] is not None:
        for res in res['Reservations']:
            print(res)




