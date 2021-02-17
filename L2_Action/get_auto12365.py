# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 16:59:42 2021

@author: HP
"""


import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
import time

def get_html(request_url):
    driver = webdriver.Chrome(executable_path='C:\Program Files\Google\Chrome\Application\chromedriver.exe')
#    request_url = 'http://www.12365auto.com/zlts/0-0-0-0-0-0_0-0-1.shtml'
    driver.get(request_url)
    time.sleep(1)
    html = driver.find_element_by_xpath("//*").get_attribute("outerHTML")
    return html

def parse_table(content):
    #通过content创建BeautifulSoup对象
    soup = BeautifulSoup(content, "html.parser", from_encoding='utf-8')
    #创建dataFrame
    df = pd.DataFrame(columns = ['id', 'brand', 'car_model', 'type', 'desc', \
                      'problem', 'datetime', 'status'])
    #找到完整的投诉信息框
    tbody = soup.find('div', class_='tslb_b')
    #找出所有的tr,即行
    tr_list = tbody.find_all('tr')
    for tr in tr_list:
        td_list = tr.find_all('td')
        #如果没有td,就是表头th
        if len(td_list) > 0:
            #投诉编号	投诉品牌	投诉车系	投诉车型	问题简述	典型问题	投诉时间	投诉状态
            id, brand, car_model, type, desc, problem, datetime, status = \
                td_list[0].text, td_list[1].text, td_list[2].text, td_list[3].text, \
                td_list[4].text, td_list[5].text, td_list[6].text, td_list[7].text
            #print (id, brand, car_model, type, desc, problem, datetime, status)
            temp = {}
            temp['id'] = id
            temp['brand'] = brand
            temp['car_model'] = car_model
            temp['type'] = type
            temp['desc'] = desc
            temp['problem'] = problem
            temp['datetime'] = datetime
            temp['status'] = status
            df = df.append(temp, ignore_index=True)
    return df
            
result = pd.DataFrame(columns = ['id', 'brand', 'car_model', 'type', 'desc', \
                      'problem', 'datetime', 'status'])

base_url = 'http://www.12365auto.com/zlts/0-0-0-0-0-0_0-0-'
page_num = 3
for i in range(page_num):
    
    request_url = base_url + str(i+1) + 'shtml'
    
    content = get_html(request_url)
    df = parse_table(content)
    result = result.append(df)

print(result)
result.to_excel('car_complain_demo.xlsx', index=False)
    




