# 说明

文件`Gross_Pricing_reservation_2020_12.json`包含了reservation和该reservation下对应的product信息。关于价格是12月份中每一天的价格，货币种类可能需要注意一下。

文件`Gross_Pricing_customers_2020_12.json`包含了customer信息，为字典格式，读取以后，可以根据customerId进行索引。

这些数据都是以json格式存储，读取以后可以变成Python中的列表或者字典。具体读取方式参照文件`read_json.py`，非常简单，读取以后就可以直接使用了。

