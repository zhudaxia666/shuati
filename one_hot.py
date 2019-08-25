'''

'''
#!/ Mypython
# -*- coding: utf-8 -*-
# @Time    : 2018/9/15 21:19
# @Author  : LinYimeng
# @File    : ceshi.py
# @Software: PyCharm
import pandas as pd
df = pd.DataFrame({"key":['green','red', 'blue'],
            "data1":['a','b','c'],"sorce": [33,61,99]})
# get_dummies(data,....) 在不指定新列的列名的情况下，将以data原标签对为列名
print("-------df---------")
print(df)
df_dummies1 =pd.get_dummies(df["key"])
print('''-------pd.get_dummies(df["key"])--df_dummies1-------''')
print(df_dummies1)
#prefix参数可以给哑变量的名字加上一个前缀
df_dummies2 =pd.get_dummies(df["key"],prefix="key")
print('''---=pd.get_dummies(df["key"],prefix="key")----df_dummies2-----''')
print(df_dummies2)
#如果不指定data列的话，默认是所有的分类变量进行one_hot处理
df_dummies3 =pd.get_dummies(df)
print("-------pd.get_dummies(df)---df_dummies3------")
print(df_dummies3)
#prefix参数可以给哑变量的名字加上一个前缀,如果是多个则需要一个列参数
df_dummies4 =pd.get_dummies(df,prefix=["class","like"])
print('''-------pd.get_dummies(df,prefix=["class","like"])----df_dummies4-----''')
print(df_dummies4)
 
 
df_dummies5 =pd.get_dummies(df,columns=["key","sorce"])
print('''---=pd.get_dummies(df,columns=["key","sorce"])----df_dummies5-----''')
print(df_dummies5)

import pandas as pd
df = pd.DataFrame({"key":['green','red', 'blue'],
            "data1":['a','b','c'],"sorce": [33,61,99]})
bins=[0,61,80,100]
'''
需要将数据划分为“0到60”，“61到79”，“79到100”几个分数组。用的是pd.cut(data,bins),这里的data是我们要分割的分数数据，bins是[0,60,79,100]。类似函数可学习pd.qcut
'''
cats=pd.cut(df["sorce"],bins)
print(cats)
group_name=["不及格","及格","优秀"]
cats2=pd.cut(df["sorce"],bins,labels=group_name,right=False)
#df["sorce"]为数据
#bins指定划分
#right指定区间闭合方向
#labels指定切分结果的标签
print(cats2)
############结果
# 0      (0, 61]
# 1      (0, 61]
# 2    (80, 100]
# Name: sorce, dtype: category
# Categories (3, object): [(0, 61] < (61, 80] < (80, 100]]
# 0    不及格
# 1     及格
# 2     优秀
# Name: sorce, dtype: category
# Categories (3, object): [不及格 < 及格 < 优秀]