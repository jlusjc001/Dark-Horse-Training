import pandas as pd
#数据加载导入数据源csv格式
df = pd.read_csv('car_complain.csv')

#拆分问题类型
df = df.drop('problem', axis = 1).join(df.problem.str.get_dummies(','))
#print(df)

#数据清洗
def f(x):
    x = x.replace('一汽-大众','一汽大众')
    return x
df['brand'] = df['brand'].apply(f)

result = df.groupby(['brand'])['id'].agg(['count'])
print(result)

#问题的标签
#tags = df.columns[7: ]
#print (tags)

#result2 = df.groupby(['brand'])[tags].agg(['sum'])
#print(result2)

#将问题的标签合并，求按品牌排序的投诉总数
#result2 = result.merge(result2, left_index = True, right_index = True, how = 'left')
#print(result2)

#result2.reset_index(inplace = True)
#print(result2)

#result2.to_csv('./L1_Action3_result.csv')

#result2 = result2.sort_values('count', ascending = False)
#print(result2)

#query = ('A12', 'sum')
#result2 = result2.sort_values(query, ascending = False)
#print(result2)


#作业部分
#按车型投诉总数
result3 = df.groupby(['car_model'])['id'].agg(['count'])
result3 = result3.sort_values('count', ascending = False)
print(result3)

#按品牌及车型投诉统计
result4 = df.groupby(['brand', 'car_model'])['id'].agg(['count'])
print(result4)

#哪个品牌车型平均投诉最多？？
#先求 mean=某品牌投诉count sum / 该品牌car_model个数， 之后sort_values('mean', ascending = False) ？
