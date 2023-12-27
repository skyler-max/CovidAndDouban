# -*- coding: utf-8 -*-

import pandas as pd
import jieba
from tkinter import _flatten
import matplotlib.pyplot as plt
from wordcloud import WordCloud


with open('stoplist.txt', 'r', encoding='utf-8') as f:
    stopWords = f.read()
StopWords = ['\n', '', ' '] + stopWords.split()

data = pd.read_csv('douban.csv', encoding='GB18030')
# Series.apply()对每一个元素运行指定的函数
# 分词
dataCut = data['短评正文'].apply(jieba.lcut)


def my_word_cloud(data=None, stopWords=None, img=None):
    # 去除停用词
    dataAfter = dataCut.apply(lambda x: [i for i in x if i not in StopWords])

    # 把二维结构数据转换为一维,并计算词频
    WordFre = pd.Series(_flatten(list(dataAfter))).value_counts()

    # 读取图片轮廓
    mask = plt.imread(img)

    # 设置字体、背景颜色
    wc = WordCloud(font_path='C:/Windows/Fonts/simfang.ttf', mask=mask, background_color='white')

    wc.fit_words(WordFre)

    plt.imshow(wc)
    plt.axis('off')

    # 展示词云
    plt.show()


index_negative = data['评分'] < 30 # 差评索引
index_positive = data['评分'] >= 30 # 好评索引

# 整体评论
my_word_cloud(data=data, stopWords=StopWords, img='aixin.jpg')
# 好评
# my_word_cloud(data=data['短评正文'][index_positive], stopWords=StopWords, img='aixin.jpg')
# 差评
# my_word_cloud(data=data['短评正文'][index_negative], stopWords=StopWords, img='aixin.jpg')
