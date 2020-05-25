## ================ 数据载入，存储及文件格式 ==================
import pandas as pd
import numpy as np
a=pd.read_csv('D:/data/ex1.csv')
print(a)
b=pd.read_table('D:/data/ex1.csv',sep=',')
print(b)
c=pd.read_csv('D:/data/ex1.csv',names=['ab','ac','ad','ae','af']) # 为表格添加列标签，不然程序会将第一列作为列表头
print(c)
names=['ab','ac','ad','ae','af']
d=pd.read_csv('D:/data/ex1.csv',names=names,index_col='af')
print(d)
print(d[1:4])
f=pd.read_csv('D:/data/ex1.csv',skiprows=[1]) #跳过数组第一行
print(f)

##### 分块读取文件，避免文件太大，读取部分
a=pd.read_csv('D:/data/ex1.csv',nrows=1) # 读取几行的标记
print(a)

# 数据写入文本格式 to_csv sys
import sys
a=pd.read_csv('D:/data/ex2.csv')
t=a.to_csv('ex2.csv')
print(t)
#print(a) ## 注意保存CSV文件时要保存成CSV格式
b=a.to_csv(sys.stdout,sep=',') # 引用SYS.stdout 可以添加任意符号
#print(b)
c=a.to_csv(sys.stdout,sep='|')
#print(c)
## 指定行列标签的是否写入
d=a.to_csv(sys.stdout,index=False,header=False) ## 去掉行列
#print(d)
f=a.to_csv(sys.stdout,index=False,columns=['a','c','d'])
#print(f) ## 选取特定的列标签所在列

## series 也有 to_csv 方法
a=pd.date_range('1/1/2000',periods=7)
b=pd.Series(np.arange(7),index=a)
print(b.to_csv)
c=pd.Series(a,index=np.arange(7))
print(c.to_csv)

## 分隔格式

## json 数据
##