# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 18:14:27 2021

@author: HP
"""


import pandas as pd

pd.set_option('max_columns', None)

# 数据加载
dataset = pd.read_csv('.\Market_Basket_Optimisation.csv', header = None)
print(dataset)
print(dataset.shape)

transactions = []
for i in range(0, dataset.shape[0]):
    temp = []
    for j in range(0, dataset.shape[1]):
        if str(dataset.values[i, j]) != 'nan':
            temp.append(dataset.values[i, j])
    transactions.append(temp)
# print(transactions)

# 挖掘频繁项集和关联规则
from efficient_apriori import apriori
itemsets, rules = apriori(transactions, min_support=0.03,  min_confidence=0.3)
print("频繁项集：", itemsets)
print("关联规则：", rules)


