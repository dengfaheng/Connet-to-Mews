import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 创建一个点数为 8 x 6 的窗口, 并设置分辨率为 80像素/每英寸
plt.figure(figsize=(8, 6), dpi=80)
# 再创建一个规格为 1 x 1 的子图
plt.subplot(1, 1, 1)

data = pd.read_csv('Gross_Pricing_all_reservations_start_utc.csv', encoding='utf-8', header=0)
dates = data['created_utc'].values.tolist()

month_num = [0 for _ in range(12)]

for date in dates:
    if date < '2020-02-01 00:00:00':
        month_num[0] = month_num[0] + 1
    elif '2020-02-01 00:00:00' <= date < '2020-03-01 00:00:00':
        month_num[1] = month_num[1] + 1
    elif '2020-03-01 00:00:00' <= date < '2020-04-01 00:00:00':
        month_num[2] = month_num[2] + 1
    elif '2020-04-01 00:00:00' <= date < '2020-05-01 00:00:00':
        month_num[3] = month_num[3] + 1
    elif '2020-05-01 00:00:00' <= date < '2020-06-01 00:00:00':
        month_num[4] = month_num[4] + 1
    elif '2020-06-01 00:00:00' <= date < '2020-07-01 00:00:00':
        month_num[5] = month_num[5] + 1
    elif '2020-07-01 00:00:00' <= date < '2020-08-01 00:00:00':
        month_num[6] = month_num[6] + 1
    elif '2020-08-01 00:00:00' <= date < '2020-09-01 00:00:00':
        month_num[7] = month_num[7] + 1
    elif '2020-09-01 00:00:00' <= date < '2020-10-01 00:00:00':
        month_num[8] = month_num[8] + 1
    elif '2020-10-01 00:00:00' <= date < '2020-11-01 00:00:00':
        month_num[9] = month_num[9] + 1
    elif '2020-11-01 00:00:00' <= date < '2020-12-01 00:00:00':
        month_num[10] = month_num[10] + 1
    else:
        month_num[11] = month_num[11] + 1

print(sum(month_num) == len(dates))
print(month_num)


def auto_label(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2. - 0.2, height+1, '%s' % int(height))


# 柱子总数
N = 12
# 包含每个柱子对应值的序列

# 包含每个柱子下标的序列
index = np.arange(N)
# 柱子的宽度
width = 0.8
# 绘制柱状图, 每根柱子的颜色为紫罗兰色
p2 = plt.bar(index, month_num, width, edgecolor='black', color="#87CEFA")
auto_label(p2)
# 设置横轴标签
plt.xlabel('Months')
# 设置纵轴标签
plt.ylabel('arrival')
# 添加标题
plt.title('Monthly Arrival, Total: '+str(len(dates)))
# 添加纵横轴的刻度
plt.xticks(index, ('Jan', 'Fub', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
plt.savefig('test3.pdf', dpi=300, bbox_inches='tight')
plt.show()
