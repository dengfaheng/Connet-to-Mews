import configparser

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# 全局设置
config = configparser.ConfigParser()
config.read('config.ini', encoding='UTF-8')
environments = config.get('CONNECT', 'Environments')




def auto_label(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2. - 0.2, height + 1, '%s' % int(height))
pass


def draw_all_years(the_plt, year_num):
    year_str = str(year_num)

    data = pd.read_csv('Gross_Pricing_all_reservations_start_utc_' + year_str + '.csv', encoding='utf-8', header=0)
    dates = data['created_utc'].values.tolist()

    month_num = [0 for _ in range(12)]

    for date in dates:
        if date < year_str + '-02-01 00:00:00':
            month_num[0] = month_num[0] + 1
        elif year_str + '-02-01 00:00:00' <= date < year_str + '-03-01 00:00:00':
            month_num[1] = month_num[1] + 1
        elif year_str + '-03-01 00:00:00' <= date < year_str + '-04-01 00:00:00':
            month_num[2] = month_num[2] + 1
        elif year_str + '-04-01 00:00:00' <= date < year_str + '-05-01 00:00:00':
            month_num[3] = month_num[3] + 1
        elif year_str + '-05-01 00:00:00' <= date < year_str + '-06-01 00:00:00':
            month_num[4] = month_num[4] + 1
        elif year_str + '-06-01 00:00:00' <= date < year_str + '-07-01 00:00:00':
            month_num[5] = month_num[5] + 1
        elif year_str + '-07-01 00:00:00' <= date < year_str + '-08-01 00:00:00':
            month_num[6] = month_num[6] + 1
        elif year_str + '-08-01 00:00:00' <= date < year_str + '-09-01 00:00:00':
            month_num[7] = month_num[7] + 1
        elif year_str + '-09-01 00:00:00' <= date < year_str + '-10-01 00:00:00':
            month_num[8] = month_num[8] + 1
        elif year_str + '-10-01 00:00:00' <= date < year_str + '-11-01 00:00:00':
            month_num[9] = month_num[9] + 1
        elif year_str + '-11-01 00:00:00' <= date < year_str + '-12-01 00:00:00':
            month_num[10] = month_num[10] + 1
        else:
            month_num[11] = month_num[11] + 1
        pass
    print(sum(month_num) == len(dates))
    # 柱子总数
    N = 12
    # 包含每个柱子对应值的序列

    # 包含每个柱子下标的序列
    index = np.arange(N)
    # 柱子的宽度
    width = 0.8
    # 绘制柱状图, 每根柱子的颜色为紫罗兰色
    p2 = the_plt.bar(index, month_num, width, edgecolor='black', color="#87CEFA")
    auto_label(p2)
    # 设置横轴标签
    # the_plt.xlabel('Months')
    # 设置纵轴标签
    the_plt.ylabel('arrival')
    # 添加标题
    the_plt.title(year_str + ' Monthly Arrival, Total: ' + str(len(dates)))
    # 添加纵横轴的刻度
    the_plt.xticks(index, ('Jan', 'Fub', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
pass


if __name__ == '__main__':
    # 创建一个点数为 8 x 6 的窗口, 并设置分辨率为 80像素/每英寸
    plt.figure(figsize=(16, 10), dpi=300)
    # 再创建一个规格为 1 x 1 的子图
    for i in range(4):
        plt.subplot(2, 2, i+1)
        year_n = 2017+i
        draw_all_years(plt, year_n)

    plt.savefig('./figure/' + environments + '_monthly_arrival.pdf', dpi=300, bbox_inches='tight')
    plt.show()
