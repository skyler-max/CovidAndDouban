# -*- coding: utf-8 -*-

import requests
import json
import pandas as pd

# --------获取中国每日疫情数据-------------------------------

C_url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_other'

res = requests.get(C_url)

text = json.loads(res.text)

data = json.loads(text['data'])

chinaDayList_data = data['chinaDayList'][0]


all_data = pd.DataFrame()
for item in data['chinaDayList']:

    date = item['date']
    confirm = item['confirm']
    suspect = item['suspect']
    dead = item['dead']
    heal = item['heal']
    importedCase = item['importedCase']
    deadRate = item['deadRate']
    healRate = item['healRate']
    updateTime = '2021/1/6'

    one_data = pd.DataFrame(
        {
            'date': date,
            'confirm': confirm,
            'suspect': suspect,
            'dead': dead,
            'heal': heal,
            'importedCase': importedCase,
            'deadRate': deadRate,
            'healRate': healRate,
            'updateTime': updateTime
        },
        index=[0]
    )

    all_data = pd.concat([all_data, one_data], axis=0)
all_data.to_csv('data/ChinaData.csv', index=None)

# ------------------------获取国内各个省份疫情数据----------------
C1_url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5'

res = requests.get(C1_url)

text = json.loads(res.text)

data = json.loads(text['data'])

china = data['areaTree']


all_data2 = pd.DataFrame()
for item2 in china[0]['children']:
    province = item2['name']
    province_confirm = item2['total']['confirm']

    one_data2 = pd.DataFrame(
        {
            'province': province,
            'province_confirm': province_confirm
        },
        index=[0]
    )

    all_data2 = pd.concat([all_data2, one_data2], axis=0)
all_data2.to_csv('data/ChinaProvinceData.csv', index=None)

# -------------------------获取外国各个国家疫情数据--------------
F_url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_foreign'

res1 = requests.get(F_url)

text1 = json.loads(res1.text)

data1 = json.loads(text1['data'])
print(data1.keys())

# foreignList为列表，每个列表元素为一个字典，字典关键字分别为：name, continent...， children代表该地区下的具体城市
# 在这里展示如何获取每个国家（不是城市）的疫情数据，若要获取具体城市，可使用children节点
F_data = data1['foreignList']


all_data1 = pd.DataFrame()
for item1 in F_data:

    country_name = item1['name']
    continent = item1['continent']
    date = item1['date']
    confirm = item1['confirm']
    suspect = item1['suspect']
    dead = item1['dead']
    heal = item1['heal']

    one_data1 = pd.DataFrame(
        {
            'name': country_name,
            'continent': continent,
            'date': date,
            'confirm': confirm,
            'suspect': suspect,
            'dead': dead,
            'heal': heal,
        },
        index=[0]
    )
    all_data1 = pd.concat([all_data1, one_data1], axis=0)
all_data1.to_csv('data/ForeignData.csv', index=None)
