# -*- coding: utf-8 -*-

'''
@Time    : 2021/1/6 14:15
@Author  : 林英超
@FileName: Table.py
@Software: PyCharm
@Description: 分析评分数量及评分与时间的关系 + 分析评论数量及评分与时间的关系
 
'''

# 未解决问题：iloc和loc

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('douban.csv', encoding='GB18030')
# num = data['评分'].value_counts()
#
# # 设置饼图——autopct：设置数据精确度
# # 设置文字编码方式
plt.rcParams['font.sans-serif'] = 'SimHei'
# plt.pie(num, autopct='%.2f %%', labels=num.index)
# plt.title(' <<流浪地球>>豆瓣短评评分分数分布')
# plt.show()

# num = data['发表时间'].apply(lambda x: x.split(' ')[0]).value_counts()
# num = num.sort_index()
#
# # 绘制折线图
# plt.plot(range(len(num)), num)
# plt.xticks(range(len(num)), num.index, rotation=45)
# plt.title('评论数量随时间的变化')
# plt.grid()
# plt.show()

# # 将时间字符串转换为时间戳并取小时数
# num = pd.to_datetime(data['发表时间']).apply(lambda x: x.hour).value_counts()
# num = num.sort_index()
# # 绘制折线图
# plt.plot(range(len(num)), num)
# plt.xticks(range(len(num)), num.index, rotation=45)
# plt.title('评论数量随时刻的变化')
# plt.grid()
# plt.show()


data.loc[:, ['发表时间', '评分']]
data['发表时间'] = data['发表时间'].apply(lambda x: x.split(' ')[0])

tmp = pd.DataFrame(0, index=data['发表时间'].drop_duplicates().sort_values(),
                   columns=data['评分'].drop_duplicates().sort_values())

# 填充tmp表格
for i, j in zip(data['发表时间'], data['评分']):
    tmp.loc[i, j] += 1

# 去除没打分的
tmp = tmp.iloc[:, : -1]

n, m = tmp.shape

# 设置画布
plt.figure(figsize=(10, 5))

# 显示负号
plt.rcParams['axes.unicode_minus'] = False
for i in range(m):
    plt.plot(range(n), (-1 if i < 2 else i)*tmp.iloc[:, i])
    # 填充颜色,设置透明度
    plt.fill_between(range(n), (-1 if i < 2 else i)*tmp.iloc[:, i], alpha=0.5)

plt.grid()
# 图例
plt.legend(tmp.columns)
plt.xticks(range(n), tmp.index, rotation=45)
plt.show()