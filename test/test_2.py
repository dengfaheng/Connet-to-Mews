# -*- coding: utf-8 -*-
"""
speed1219.csv data file format:
dtime,speed
2017-12-19 10:33:30,803
2017-12-19 10:35:29,1008
2017-12-19 10:36:04,1016
2017-12-19 10:37:32,984
2017-12-19 10:38:06,1008
"""
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import AutoDateLocator, DateFormatter

df = pd.read_csv('speed.csv', parse_dates = ['dtime'])
plt.plot_date(df.dtime, df.speed, fmt='b.')

ax = plt.gca()
ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d %H:%M'))  # 设置时间显示格式
ax.xaxis.set_major_locator(AutoDateLocator(maxticks=24))  # 设置时间间隔

plt.xticks(rotation=90, ha='center')
label = ['speedpoint']
plt.legend(label, loc='upper right')

# plt.grid()

ax.set_title(u'传输速度', fontproperties ='SimHei', fontsize = 14)
ax.set_xlabel('dtime')
ax.set_ylabel('Speed(KB / s)')

plt.show()
