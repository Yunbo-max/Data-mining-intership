import pandas as pd

#pandas 最核心的结构
food_info =  pd.read.csv("food.csv")
print(help(pd.read.csv))

food_info.head(6)
food_info.tail(5)
print(food_info.columns)
print(food_info.shape)
print(food_info.loc[0:4])
x = food_info["列名","adfs"][age_null == False]
a = food_info.columns.tolist()

b=[]
for i in a:
    if a.endswith("(g)"):
        b.append(i)

food_info.sort_values("列表",inplace = True,ascecnding = False)


null = pd.isnull(age)
true1 = age[null]

answer = food_info.pivot_table(index = "",values=" ")

food_info = food_info.apply(lambda x: np.std(x),axis = 1) #返回这一项的所有内容，自定义函数


from pandas import Series
custom = Series(scores,index = name)#将索引变成名字而不再是数字
custom['']

