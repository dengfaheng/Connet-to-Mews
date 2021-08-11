# 导入第三方包
import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

import matplotlib.mlab as mlab

# 中文和负号的正常显示

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False

# 读取Titanic数据集

titanic = pd.read_csv('titanic.csv')

# 检查年龄是否有缺失any(titanic.Age.isnull())

# 不妨删除含有缺失年龄的观察

titanic.dropna(subset=['age'], inplace=True)

# 设置图形的显示风格

# plt.style.use('ggplot')

# 绘图：乘客年龄的频数直方图
# 绘图数据
# 指定直方图的条形数为20个
# 指定填充色
# 指定直方图的边界色
plt.hist(titanic.age, bins=6, color='steelblue', edgecolor='k', label='直方图') # 为直方图呈现标签

# 去除图形顶部边界和右边界的刻度

plt.tick_params(top='off', right='off')
# index = np.arange(6)
# plt.xticks(index, ('Jan', 'Fub', 'Mar', 'Apr', 'May', 'Jun'))

# 显示图例

plt.legend()

# 显示图形

plt.show()

