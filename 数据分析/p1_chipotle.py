import numpy as np
import pandas as pd
from pandas import Series, DataFrame

path="chipotle.tsv"
df=pd.read_csv(path,sep="\t")
#1.查看数据集的结构
df.shape
#2.当前数据集有哪些列
df.columns
#3.这些列都是什么类型的
df.info()
#4.查看前10行的数据
df.head(10) #默认展示5行
#5.查看后10行的数据
df.tail(10)
#6.每一件商品被下单多少次（每个item在整个数据集中出现多少次）
df["item_name"].value_counts(ascending=True) #默认是降序
#  value_counts()是一种查看表格某列中有多少个不同值的快捷方法，并计算每个不同值有在该列中有多少重复值。

#7.当前数据集中一共有多少商品被下单
#(1)--
df["item_name"].nunique() #不重复的item
#(2)--
df["item_name"].value_counts().shape(0)

#8.查看choice_description中出现的次数最多的是什么
df["choice_description"].value_counts().head(1)
#9.数据集中订单商品数量的和（统计quantity字段的和）
df["quantity"].sum()

#10.新加一列，用来存放每条记录的交易价格
  #对某一列进行统计的算法操作或处理，可以使用apply()函数,该函数中的参数可以是一个函数也可以是一个lamda表达式
  #(1)---
def str2float(x):
      #x-->$9.25-->9.25
    return float(x[1:])
df["item_price"].apply(str2float)
  #(2) ---
df["item_price_float"] = df["item_price"].apply(lambda x: float(x[1:]))

#11.计算当前数据集的总交易额
df["item_price_float"].sum()

#12.当前数据集中一共有多少订单
df.order_id.nunique()
df["order_id"].value_counts().count()

#13.分别计算每一单的总价，然后将每单总价放在一起计算一个平均值
#这里需要用到分组函数
df.groupby(["order_id"]).sum().mean()["item_price_float"]