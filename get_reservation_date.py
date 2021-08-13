import requests
import json
import configparser
from datetime import datetime
from datetime import timedelta
import time
import pandas as pd

# 全局设置
config = configparser.ConfigParser()
config.read('config.ini', encoding='UTF-8')
client_token = config.get('CONNECT', 'ClientToken')
access_token = config.get('CONNECT', 'AccessToken')
client_name = config.get('CONNECT', 'Client')
platform_address = config.get('CONNECT', 'PlatformAddress')
environments = config.get('CONNECT', 'Environments')
utc_format = config.get('CONNECT', 'UtcFormat')


def get_post_data() -> dict:
    temp_post_data = {
        "ClientToken": client_token,
        "AccessToken": access_token,
        "Client": client_name
    }
    return temp_post_data


# end def


def get_all_service_id() -> list:
    connect_url = platform_address + 'api/connector/v1/services/getAll'
    post_data = get_post_data()
    resp = requests.post(url=connect_url, data=json.dumps(post_data))
    resp = json.loads(resp.text)
    service_id_list = []
    for service in resp['Services']:
        service_id_list.append(service['Id'])
    return service_id_list


# end def

def get_a_batch_reservations(post_data: dict) -> dict:
    connect_url = platform_address + 'api/connector/v1/reservations/getAll'
    resp = requests.post(url=connect_url, data=json.dumps(post_data))
    resp = json.loads(resp.text)
    return resp

# end def


def get_all_reservation_start_utc(start_utc_str, weeks_num):
    post_data = get_post_data()
    post_data['ServiceIds'] = ["bd26d8db-86da-4f96-9efc-e5a4654a4a94"]
    post_data['TimeFilter'] = 'Created'
    post_data['Extent'] = {
        "Reservations": True,
        "ReservationGroups": False,
        "Customers": False
    }
    this_start_utc = datetime.strptime(start_utc_str, utc_format)
    all_reservations_list = []
    for i in range(weeks_num):
        this_start_utc_str = this_start_utc.strftime(utc_format)
        post_data['StartUtc'] = this_start_utc_str
        this_end_utc = this_start_utc + timedelta(days=6)
        post_data['EndUtc'] = this_end_utc.strftime(utc_format)
        batch_reservations = get_a_batch_reservations(post_data)
        # print(batch_reservations)
        all_reservations_list.extend(batch_reservations['Reservations'])
        # 下一周的
        this_start_utc = this_start_utc + timedelta(weeks=1)
        print("get ", len(batch_reservations['Reservations']))
        time.sleep(1)
    pass
    # 按时间先后排序
    all_reservations_list = sorted(all_reservations_list, key=lambda x: x['CreatedUtc'], reverse=False)
    # 获取时间
    base_utc = datetime.strptime(start_utc_str, utc_format)
    created_utc_list = []
    order_list = []
    for reservation in all_reservations_list:
        created_utc_str = reservation['CreatedUtc']
        created_utc = datetime.strptime(created_utc_str, utc_format)
        position = int((created_utc - base_utc).total_seconds())
        created_utc_list.append(created_utc.strftime('%Y-%m-%d %H:%M:%S'))
        order_list.append(position)
    # 写入文件保存起来
    data_frame = pd.DataFrame({'created_utc': created_utc_list, 'order': order_list})
    data_frame.to_csv(environments+"_all_reservations_start_utc_2017.csv", index=False, sep=',')

    with open(environments+"_all_reservations_2017.json", "w+") as json_file:
        json_file.write(json.dumps(all_reservations_list, indent=4))
    pass


# end def

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    get_all_reservation_start_utc('2017-01-01T00:00:00Z', 52)
