# 求2+4+6+...+100的和
sum = 0
for i in range(1, 101):
    if i % 2 == 0:
        sum = sum + i
        print("i =", i, "sum =",sum)
print ("和为：", sum)
