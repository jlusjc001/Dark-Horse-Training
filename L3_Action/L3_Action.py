# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 21:06:38 2021

@author: HP
"""


# 汽车消费城市划分
from sklearn.cluster import KMeans
from sklearn import preprocessing
import pandas as pd
import numpy as np

# 数据加载
data = pd.read_csv('car_data.csv', encoding='gbk')
print(data)
train_x = data[['人均GDP', '城镇人口比重', '交通工具消费价格指数', '百户拥有汽车量']]

# 规范化到[0, 1]空间
min_max_scaler = preprocessing.MinMaxScaler()
train_x = min_max_scaler.fit_transform(train_x)
pd.DataFrame(train_x).to_csv('temp.csv', index=False)
print(train_x)

# 使用KMeans聚类
kmeans = KMeans(n_clusters=4)
predict_y = kmeans.fit_predict(train_x)

result = pd.concat((data, pd.DataFrame(predict_y)), axis=1)
result.rename({0: u'聚类结果'}, axis=1, inplace=True)
print(result)
result.to_csv('customer_cluster_result.csv', index=False)


# K-Means 手肘法：统计不同K取值的误差平方和
import matplotlib.pyplot as plt
sse = []
for k in range(1, 11):
    # kmeans算法
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(train_x)
    # 计算inertia簇内误差平方和
    sse.append(kmeans.inertia_)
x = range(1, 11)
plt.xlabel('K')
plt.ylabel('SSE')
plt.plot(x, sse, 'o-')
plt.show()
