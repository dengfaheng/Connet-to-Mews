# 说明

文件`Gross_Pricing_reservation_2020_12.json`包含了reservation和该reservation下对应的product信息。关于价格是12月份中每一天的价格，货币种类可能需要注意一下。

文件`Gross_Pricing_customers_2020_12.json`包含了customer信息，为字典格式，读取以后，可以根据customerId进行索引。

这些数据都是以json格式存储，读取以后可以变成Python中的列表或者字典。具体读取方式参照文件`read_json.py`，非常简单，读取以后就可以直接使用了。


# 2021-09-16 更新
更新了两个文件：
- `Gross_Pricing_reservation_2020_12new1.json`中只包含那些type是room的reservation，其他的什么department啊我去掉了。只有120条数据
- `Gross_Pricing_reservation_2020_12new2.json`包含了所有的type，什么suite，department，room等。有200多条数据

每个字典中，如果含有key `rates`和`Currency`，说明这条reservation的rates是能检索到的。我就把12月份的价格数据检索出来了。Currency货币单位可能需要注意一下。

如果没有key `rates`和`Currency`，那么说明这条reservation的rates是无法检索的。

其他的关于你说的time啊什么的，都在里面了，product type是`RequestedCategoryId`这个key，然后`countInMonth`记录了这条category一个月内被预定了几次。统计的话，是根据不同文件统计的，比如`Gross_Pricing_reservation_2020_12new1.json`就是通过它中的120条数据统计的出现次数。

