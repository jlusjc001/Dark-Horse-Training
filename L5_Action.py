# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 19:00:32 2021

@author: HP
"""


import pandas as pd

pd.set_option('max_columns', None)

# 数据加载
dataset = pd.read_csv('.\Market_Basket_Optimisation.csv', header=None)
# print(dataset)
# print(dataset.shape)

# 将数据存入transactions,并建立字典存储items和出现的次数
transactions = []
item_count = {}
for i in range(0, dataset.shape[0]):
    temp = []
    for j in range(0, dataset.shape[1]):
        item = str(dataset.values[i, j])
        if item != 'nan':
            temp.append(item)
            if item not in item_count:
                item_count[item] = 1
            else:
                item_count[item] += 1
    transactions.append(temp)
# print(transactions)

from wordcloud import WordCloud
from nltk.tokenize import word_tokenize

# 去除停用词，在此例中没有明显的停用词
def remove_stop_words(f):
    stop_words = []
    for stop_word in stop_words:
        f = f.replace(stop_word, ' ')
    return f

# 生成词云
def creat_word_cloud(f):
    f = remove_stop_words(f)
# 将字符串分词
    cut_text = word_tokenize(f)
# 将分词用空格连接
    cut_text = " ".join(cut_text)
    wc = WordCloud(
        max_words=100,
        width=2000,
        height=1200,
        )
    wordcloud = wc.generate(cut_text)
    wordcloud.to_file("wordcloud.jpg")

# 将marketbasket生成词云
all_word = ' '.join('%s' % item for item in transactions)
creat_word_cloud(all_word)

# 输出Top10的商品
top10 = sorted(item_count.items(), key=lambda x: x[1], reverse=True)[: 10]
print(top10)