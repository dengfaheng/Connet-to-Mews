import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.dates as mdates
from datetime import datetime

plt.rcParams['font.sans-serif'] = ['SimHei']  # 解决中文无法显示的问题
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


def draw_time_text(dates, dateFormat="%Y-%m-%d %H:%M:%S", levels=None):
    # 转换类型 date strings (e.g. 2020-01-01 08:47:58) to datetime
    dates = [datetime.strptime(d, dateFormat) for d in dates]
    if levels == None:
        # Choose some nice levels
        levels = [0 for _ in range(len(dates))]
    # Create figure and plot a stem plot with the date
    fig, ax = plt.subplots(figsize=(100, 10), constrained_layout=False)
    # 标题
    my_title = 'customer arrival, total: '+str(len(dates))
    ax.set(title=my_title)

    # 添加线条, basefmt设置中线的颜色，linefmt设置线的颜色以及类型
    markerline, stemline, baseline = ax.stem(dates, levels)
    # 交点空心,zorder=3设置图层,mec="k"外黑 mfc="w"内白
    plt.setp(markerline, mec="k", mfc="w", zorder=3)

    # 通过将Y数据替换为零，将标记移到基线
    markerline.set_ydata(np.zeros(len(dates)))

    # 设置x轴间隔为每1个月
    ax.get_xaxis().set_major_locator(mdates.MonthLocator(interval=1))
    ax.get_xaxis().set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))
    # 逆时针30度，刻度右对齐
    plt.setp(ax.get_xticklabels())

    # 隐藏y轴线
    ax.get_yaxis().set_visible(False)
    # 隐藏左、上、右的边框
    for spine in ["left", "top", "right"]:
        ax.spines[spine].set_visible(False)
    # 边距仅设置y轴
    ax.margins(y=0.1)
    plt.savefig('test2.pdf', dpi=300, bbox_inches='tight')
    plt.show()


if __name__ == '__main__':
    data = pd.read_csv('Gross_Pricing_all_reservations_start_utc.csv', encoding='utf-8', header=0)
    dates = data['created_utc'].values.tolist()

    draw_time_text(dates)
