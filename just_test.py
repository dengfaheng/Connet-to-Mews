from datetime import datetime
from datetime import timedelta

utc_time_str = '2016-01-01T00:00:00Z'
utc_time_str2 = '2016-11-01T00:10:00Z'
utc_format = '%Y-%m-%dT%H:%M:%SZ'

utc_dt = datetime.strptime(utc_time_str, utc_format)

print(utc_dt)
print('hhh', utc_dt.strftime('%Y-%m-%d %H:%M:%S'))

utc_dt2 = datetime.strptime(utc_time_str2, utc_format)
print((utc_dt2 - utc_dt).total_seconds())
utc_dt = utc_dt + timedelta(days=6)



import configparser

#  实例化configParser对象
config = configparser.ConfigParser()
# -read读取ini文件
config.read('config.ini', encoding='UTF-8')
# -sections得到所有的section，并以列表的形式返回
print('ClientToken: ',  config.get('CONNECT', 'UtcFormat'))

client_token = config.get('CONNECT', 'ClientToken')
access_token = config.get('CONNECT', 'AccessToken')
client_name = config.get('CONNECT', 'Client')


my_dict = [
    {"1": "2016-01-01T20:00:00Z"},
    {'1': '2016-01-01T00:10:00Z'},
    {'1': '2016-01-01T10:00:00Z'}
]

print(my_dict)

print(int(1.0))


import pandas as pd

#任意的多组列表
a = [1,2,3]
b = [4,5,6]

#字典中的key值即为csv中列名
dataframe = pd.DataFrame({'a_name': a, 'b_name': b})

#将DataFrame存储为csv,index表示是否显示行名，default=True
# dataframe.to_csv("test.csv", index=False, sep=',')


lis = my_dict

ls = sorted(lis, key=lambda x: x['1'], reverse=False)

print(ls)
