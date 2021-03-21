# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 17:42:21 2021

@author: HP
"""


import pandas as pd
from fbprophet import Prophet
# 数据加载
train = pd.read_csv('./train.csv')


# 转换为pandas日期格式
train['Datetime'] = pd.to_datetime(train['Datetime'])


# 将Datetime作为index, 删除不需要的Datetime和ID列
train.index = train['Datetime']
train.drop(['ID', 'Datetime'], axis=1, inplace=True)

# 按照天进行累计采样
daily_train = train.resample('D').sum()
daily_train['ds'] = daily_train.index
daily_train['y'] = daily_train['Count']
daily_train.drop(['Count'], axis=1, inplace=True)
print(daily_train)


# 创建模型
m = Prophet(yearly_seasonality=True, seasonality_prior_scale=0.1)
m.fit(daily_train)

# 预测未来7个月
future = m.make_future_dataframe(periods=213)

forecast = m.predict(future)
print(forecast)
m.plot(forecast)
