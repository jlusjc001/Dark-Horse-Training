import pandas as pd

data = {"mame": pd.Series(["Zhang Fei", "Guan Yu", "Liu Bei", "Dian Wei", "Xu Chu"]),
        "Chinese": pd.Series([68, 95, 98, 90, 80]),
        "Math": pd.Series([65, 76, 86, 88, 90]),
        "English": pd.Series([30, 98, 88, 77, 90])
        }
df = pd.DataFrame(data)
print(df)

#整体统计描述
print("整体统计描述：")
print(df.describe())

#平均成绩
print("平均成绩")
print(df.mean())

#最小成绩  ??如何不统计第一列（姓名列）？
print("最小成绩")
print(df.min())

#最大成绩
print("最大成绩")
print(df.max())

#方差
print("方差")
print(df.var())

#标准差
print("标准差")
print(df.std())
