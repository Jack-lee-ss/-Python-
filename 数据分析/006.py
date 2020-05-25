##================ pandas ======================
from pandas import Series,DataFrame
import pandas as pd
import numpy as np
a=pd.Series([1,2,3,4]) ## 与numpy类似，不同在于可以输出索引
print(a)
print(a.values) #获取值
print(a.index) #获取索引初始值

## 创建索引类型
a=pd.Series([1,2,3,4],index=['a','b','c','d'])
print(a)
print(a['c']) # 通过索引值获取相应数值
print(a[['a','d']]) # 获取多个数值的索引要加[],字符串的索引列表
b=a[0]*2
print(b) # 输出单个的数值数学运算后的结果
print(a*2) # 输出整个数值数学运算后的结果，包括索引，不变

## 使用字典输出
a={'a':1,'b':2,'c':3}
b=pd.Series(a) #将字典键作为索引，值作为数值
print(b)

## 构造列表作为字典的键，从而输出相应的索引,列表值只能是重新排序的字典键
a=['string','a','b']
b={'a':1,'b':2,'c':3}
c=pd.Series(b,index=a)
print(c)

### DataFrame 二维，矩阵数据表
a={'state':['book','tabe','bottle'],'year':[2019,2018,1027],'pop':[1.2,3.5,6.8]}
b=pd.DataFrame(a)
print(b)
b=pd.DataFrame(a,columns=['year','state','pop']) #设定列标签
print(b)
print(b['state']) # 按字典标记检索
print(b.state) ## 等价同上结果
print(b.year)

## 可以修改，添加列标签
c=pd.DataFrame(a,columns=['year','state','pop','deta'])
c['deta']='s'
print(c)

#### Series 和 DataFrame 结合
a={'state':['book','tabe','bottle'],'year':[2019,2018,1027],'pop':[1.2,3.5,6.8]}
b=pd.DataFrame(a,columns=['state','year','pop','deta'])# 加列标签
#c=b['deta']=np.arange(3.) # 新生成的列标签赋值
b['deta']=pd.Series([1,4,7],index=[0,1,2])
print(b) # 输出新列表
# index 可以根据 DataFrame 的行标签配对，给新的列标签输入数据
## 创建新列，布尔值列
b['bools']=b['year']==2019 #如果
print(b)
del b['bools'] # 删除新增bools列
print(b)
print(b.columns) ## 同上，可以查到删除后的列标签

## 嵌套字典赋给DataFrame
a={'a':{1:100,2:200},'b':{3:300,4:400,5:500}}
b=pd.DataFrame(a) #字典键作为列标签，内部键作为行标签
print(b)
c=pd.DataFrame(a,index=[1,2,3]) #取特定内部键值的标签
print(c)
print(c.values) # 查看序列内容
print(c.columns) # 参看序列列标签

### 索引对象
a=pd.Series(range(3),index=['a','b','c'])
print(a)
print(a.index)
print(a.index[1]) ## 查找具体索引值
# a.index[1]=4 错误，索引对象是不可变的，无法赋新值
# 索引对象是一个集合，可以查看某个值是否在其中
i='a' in a.index
print(i) ## 返回结果，是否有 a
print()

#### 索引一些用法
## 重建索引
a=pd.Series([1,2,3.4,5],index=['d','a','b','e'])
print(a)
b=a.reindex(['a','b','c','d']) ## 重置旧索引，新加索引无值的记NAN
print(b)
a=pd.Series(['blue','black','green','red'],index=[0,4,5,6])
print(a)
b=a.reindex(range(6),method='ffill')
print(b) ## method=ffill：重建索引，在原索引第一个后添加值
a=pd.Series(['blue','black','green','red'],index=[3,4,5,6])
b=a.reindex(range(6),method='ffill') ##重建索引前几个为缺失值
print(b) ## ffill 向前填充，bfill 向后填充

### DataFrame中，reindex
a=pd.DataFrame(np.arange(9).reshape((3,3)),index=['a','b','c'],columns=['red','black','green'])
print(a) ## 设置索引行与列的表单
b=a.reindex(['a','c','c','d']) #重建行索引，新添加为缺失值
print(b)
c=a.reindex(columns=['red','black','vba','green'])
print(c) ## 添加新列或者重新排列其顺序，如果列标签变了，则出现缺失值

## 更为简洁的标签引用方式
d=a.loc[['b','c','a'],['black','red','green']]
print(d)

## 删除索引或者列标签所在行列
# series 中
a=pd.Series(np.arange(4),index=['a','b','c','d'])
b=a.drop('a')
print(b)
b=a.drop(['a','c']) ## 删除两行数据
print(b)
c=a.drop('c',inplace=True) ## 会删除原数据，a 中不会存在 c 行
print(a)

## DataFrame
a=pd.DataFrame(np.arange(9).reshape((3,3)),index=['a','b','c'],columns=['red','black','green'])
b=a.drop(['red'],axis='columns') ## 删除列，一列
print(b)
c=a.drop(['black','green'],axis='columns') ##删除两列
print(c)

#### 索引，选择，修改行列标签的值
a=pd.Series(np.arange(4),index=['a','b','c','d'])
print(a[['a','b']]) ## 索引行值
print(a[a<2]) ## 索引行号大小值
print(a[2:4]) ## 索引切片
a['b':'c']=76 ## 修改行号内容
print(a)

a=pd.DataFrame(np.arange(9).reshape((3,3)),index=['a','b','c'],columns=['red','black','green'])
print(a[['red','black']]) ## 选取两列，用列表
print(a['red']) ##单列选取，无列标签
print(a.drop(['a','b'])) ## 行号选取可以删除不需要的行留下需要的行

## 特殊选取 布尔值数组切片 ,可以选行，行选语法
print(a[:1]) # 选择第一行
print(a[a['black']>3]) # 行选语句，选择行数值中大于3的行
a[a['black']>3]=0 ## 对标量赋值
print(a)

### loc（轴标签）和iloc（整数标签）选择数据 ------ 选择DataFrame中的行列子集
a=pd.DataFrame(np.arange(9).reshape((3,3)),index=['a','b','c'],columns=['red','black','green'])
print(a.loc['b',['red','green']]) #选取行标签和相应列标签的值

print(a.iloc[1,[2,0,1]]) ## 行数组，列数组，获取数值
print(a.iloc[1]) # 单个中括号一个数字指行数组
print(a.iloc[[1,2],[0,1,2]]) #各取[1,2]数组行的[0,1,2]列数据，注意：前一个中括号内，第一个数为行数组，第二个数为列数组，后一个中括号为对应列。
print(a.loc[:'b','black']) ## 行号切片，列号取标签
print(a.iloc[:,:1][a>2]) ## 切片加运算

### 算术和数据对齐
a=pd.Series([1.4,3.5,5.7],index=['a','b','c'])
b=pd.Series([-2.4,5.7,9.8],index=['b','g','a'])
print(a+b) ## 有相同标签的相加，无重叠的记为缺失值
a=pd.DataFrame(np.arange(9).reshape((3,3)),columns=['b','c','d'],index=['red','black','blue'])
b=pd.DataFrame(np.arange(12).reshape((4,3)),columns=['b','d','e'],index=['white','red','blue','pear'])
print(a+b) ## 相同行列标签才可以运算，无交集者记为NAN缺失值，注：columns=['b','d','e'] 等价 columns=list('bde')
a=pd.DataFrame({'A':[1,2]}) #'A':列标签，[1,2]：列标签值
b=pd.DataFrame({'B':[3,4]})
print(a-b) ## 行列均不同运算为NAN

### 使用填充值的算术方法
a=pd.DataFrame(np.arange(12.).reshape((3,4)),columns=list('abcd'))
b=pd.DataFrame(np.arange(20.).reshape((4,5)),columns=list('abcde'))
print(a+b) ## 无公共交集的记为NAN，避免NAN出现，使用add方法，传入参数 fill_value
print(a.add(b,fill_value=0)) ## 在 a 的基础上附上 b和fill_value 的值，fill_value相当于 a 比 b 少的部分记为0，再加上 b 的值的结果
print(a.reindex(columns=b.columns,fill_value=0))## 不同填充值

## 数组的广播机制
a=np.arange(12.).reshape(3,4)
print(a-a[0]) ## 每一行都减去 a[0]的值

## DataFrame Series中相同
a=pd.DataFrame(np.arange(9).reshape((3,3)),columns=['b','c','d'],index=['red','black','blue'])
print(a)
b=a.iloc[1] ## 行号
print(b)
print(a-b) ## 每一行均减去 iloc[1] ---------减行

c=pd.Series(range(3),index=['a','b','d'])
print(c+a) ## 此时，series中的行索引可以与DateFrame中的列索引相匹配，因为两者索引有相同项，无交集者记为NAN。相应列加上c 的对应值
print(c-a) # 各列减去 c 的对应值

## 另一种列上广播-----减列
a=pd.DataFrame(np.arange(9).reshape((3,3)),columns=['b','c','d'],index=['red','black','blue'])
b=a['c']
print(a.sub(b,axis='index')) ##先选定一列，在将原数据各列均减去该列

#### 函数应用和映射

## 排序和排名
# Series 中
a=pd.Series(range(4),index=['d','a','c','b'])
print(a.sort_index()) ## 等价 print(a.sort_index(axis=0)),表示：只排序行号，索引号，默认从小到大。

b=pd.Series([3,-8,9,4,np.nan])
print(b.sort_values()) ## 只排序值大小，从小到大，缺失值放在最底层

## DateFrame 中
# 按行列标签排序
a=pd.DataFrame(np.arange(9).reshape((3,3)),columns=['b','f','d'],index=['two','one','three'])
print(a.sort_index()) ## 等价下式
print(a.sort_index(axis=0)) ## 只改变行索引排序
print(a.sort_index(axis=1)) ## 只改变列索引排序
## 降序排法
print(a.sort_index(axis=0,ascending=False)) ## 0轴行轴降序
print(a.sort_index(axis=1,ascending=False)) ## 1轴列轴降序

## 按列标签所在列的值大小排序，分为单列和多列
a=pd.DataFrame({'b':[9,-7,3,5],'a':[3,0,-7,5]})
print(a) ## 字典转为DateFrame
print(a.sort_values(by='b')) # 传入 by 参数，选择指定列，排序值
print(a.sort_values(by=['a','b'])) # 多列排序

## 排名 rank函数
a=pd.Series([7,-5,7,4,2,0,4])
print(a.sort_values()) # 数值列从小到大，-5 第一，依次下去
print(a.rank()) # 原列表中，7在第一位，但在上式中在6,7位，所以取平均值6.5， -5在第二位，但在上式中在第一位，记为1.0 ，依次类推，得到源列表的rank函数，如下。

#### 含重复标签的索引
a=pd.Series([1,2,3,4],index=['a','b','a','c'])
print(a.index.is_unique) ## is_unique 判断标签是否唯一，布尔值
print(a['a']) ## 重复标签都返回
a=pd.DataFrame(np.arange(9).reshape((3,3)),columns=['b','f','b'],index=['one','one','three'])
print(a['b']) #返回两列数
print(a.loc['one']) # 返回两行

### 描述性计算
# describe
a=pd.DataFrame(np.arange(9).reshape((3,3)),columns=['b','f','d'],index=['two','one','three'])
print(a.describe()) # 各列汇总统计
b=pd.Series(['a','b','c']*4)
print(b.describe()) # 汇总统计
## 唯一值，计数，属性包含关系
a=pd.Series(['a','b','c','a','a'])
print(a.unique()) # 提取不重复值
print(a.value_counts()) # 不重复值的计数
b=pd.value_counts(a.values,sort=False)
print(b) ## 按数量降序排列
print(a.isin(['a','b'])) ## 属于包含关系
print(a[a.isin(['a','b'])]) # 输出相应内容















