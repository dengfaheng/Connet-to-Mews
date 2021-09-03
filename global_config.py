# 全局设置
import configparser


config = configparser.ConfigParser()
config.read('config.ini', encoding='UTF-8')
client_token = config.get('CONNECT', 'ClientToken')
access_token = config.get('CONNECT', 'AccessToken')
client_name = config.get('CONNECT', 'Client')
platform_address = config.get('CONNECT', 'PlatformAddress')
environments = config.get('CONNECT', 'Environments')
utc_format = config.get('CONNECT', 'UtcFormat')