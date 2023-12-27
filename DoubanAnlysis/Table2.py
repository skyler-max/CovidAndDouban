# -*- coding: utf-8 -*-

# 未解决问题：for循环

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('douban.csv', encoding='GB18030')
num = data['居住城市'].value_counts()[:10]

plt.rcParams['font.sans-serif'] = 'SimHei'
plt.bar(range(10), num)
plt.xticks(range(10), num.index, rotation=45)
plt.title('评论数量最多的前十个城市')

for i, j in enumerate(num):
    plt.text(i, j, j, ha='center', va='bottom')
plt.show()

tmp = pd.DataFrame(0,
                   index=data['评分'].drop_duplicates().sort_values(), columns=data['居住城市'].drop_duplicates())

for i, j in zip(data['评分'], data['居住城市']):
    tmp.loc[i, j] += 1

cities = num.index[:5]
# 选取评论数前五的城市数据
tmp = tmp.loc[:, cities]
# 去除nan评分数据
tmp = tmp.iloc[:5, :]

n, m = tmp.shape
plt.figure(figsize=(10, 5))
plt.rcParams['axes.unicode_minus'] = False
for i in range(m):
    plt.plot(range(n), tmp.iloc[:, i])
    plt.fill_between(range(n),tmp.iloc[:, i], alpha=0.5)
plt.grid()
plt.title('评论评分与城市的关系')
plt.legend(tmp.columns)
plt.xticks(range(n), tmp.index, rotation=45)
plt.show()
