## ============ 数据规整：连接、联合与重塑 pandas =============

import numpy as np
import pandas as pd
from numpy import nan as NA
import warnings
warnings.filterwarnings("ignore") ##出现warning时，可以忽略

## 分层索引:低纬度形式处理高纬度数据
a=pd.Series(np.random.randn(9),index=[['a','a','a','b','b','c','c','d','d'],[1,2,3,1,3,1,2,2,3]])
print(a) ## 第一列重复索引使用上面的值
print(a.index) ## 将两列索引对应起来
print(a['a']) # 获取a标签的所有数据
print(a['a',3]) #获取a标签下3标签的数据
print(a['b':'c']) ## 获取两个标签的数据 b 到 c列的数据 切片数据
print(a.loc[['a','c']]) ## 单独获取 a c标签的数据，非连续标签
print(a.loc[:,3]) ## 内部标签中，索引是3的行数据
print(a.loc[:'c',2]) ##  a到c标签中，内标签是2的数值

print(a.unstack()) # unstack函数重排数据
print(a.unstack().stack()) ## 再重排

## 分层索引----行列
a=pd.DataFrame(np.random.randn(12).reshape((4,3)),index=[['a','a','b','b'],[1,2,1,2]], columns=[['oh','oh','cop'],['gbk','rty','green']])
print(a)
a.index.names=['k1','k2']  ## 给行列标签添加名称
a.columns.names=['b1','b2']
print(a)
print(a['oh']) ## 部分列索引，必须用最高的列标签索引
print(a.swaplevel('k1','k2')) ## 调换内外层级顺序
print(a.sort_index(level=0)) ## 对外层级排序，从小到大
print(a.sort_index(level=1)) ## 对内层级排序，小到大
print(a.swaplevel('k1','k2').sort_index(level=0)) ## 调换内外层级后再对外层及排序，level=0/1   代表层级内外

## 按层级汇总统计-----level
a=pd.DataFrame(np.random.randn(12).reshape((4,3)),index=[['a','a','b','b'],[1,2,1,2]], columns=[['oh','oh','cop'],['gbk','rty','green']])
a.index.names=['k1','k2']
a.columns.names=['b1','b2']
print(a.sum(level='k2')) ## 汇总或者提取'k2'标签下所有数据
print(a.sum(level='b2',axis=1))  #### ?????

### 使用DateFrame列进行索引
a=pd.DataFrame({'a':range(7),'b':range(7,0,-1),'c':['one','one','one','two','two','two','two'],'d':[0,1,2,0,1,2,3]})
print(a)
print(a.set_index(['c','d'])) ## 创建新的函数，使用一列或者多列作为索引
print(a.set_index(['c','d'],drop=False)) ## 默认会删除新生成的c,d 列，drop=flase可以留下

## 联合与合并数据集 pandas.merge/concat...
## 表中列标签相同时
a=pd.DataFrame({'key':['b','b','a','c','a','a','b'],'data1':range(7)})
b=pd.DataFrame({'key':['a','b','d'],'data2':range(3)})
print(pd.merge(a,b))
print(pd.merge(b,a))
## 注：a b两列中a列存在重复行内容，b列则都为唯一行内容，merge函数，取交集，pd.merge(a,b):b连在a后面，先将ab列重复值取出，b列没有多余行则用唯一值补全。同理，pd.merge(a,b)亦如此。
## 可以显式的指定重叠列
print(pd.merge(a,b,on='key')) ##效果同上

### how参数选项总结：默认情况下：merge是内连接，即键是两张表的交集，并集外连接是outer，left连接是merge的第一个参数，right是第二个参数，如：merge(a,b,on='key')，left是a,right是b merge(a,b,on='key'，how='left') ：左连接加交集的并集

a=pd.DataFrame({'key':['b','b','a','c','a','b'],'data1':range(6)})
b=pd.DataFrame({'key':['a','b','a','b','d'],'data2':range(5)})
print(pd.merge(a,b,on='key',how='left'))
## 多对多连接是行的笛卡尔积，两表中均有重复值，分别连接，缺失值补NAN
print(pd.merge(a,b,how='inner'))
print(pd.merge(a,b,how='outer')) ## 并集

## 多个键合并，多列合并
left=pd.DataFrame({'k1':['foo','foo','bar'],'k2':['one','two','one'],'lval':[1,2,3]})
right=pd.DataFrame({'k1':['foo','foo','bar','bar'],'k2':['one','one','one','two'],'rval':[4,5,6,7]})
print(pd.merge(left,right,on=['k1','k2'],how='outer'))
### on=['k1','k2']：以同时满足两列的数值求并集
print(pd.merge(left,right,on=['k1','k2'],how='inner'))#交集

print(pd.merge(left,right,on='k1')) ### ???
print(pd.merge(left,right,on='k1',suffixes=('_left','_right')))  ### ????

## 列标签不同时，行索引和列的数值有相同项
##### 索引合并：将符合条件的行索引提取出来，不用默认从0开始的索引，用交集的实际索引。
left1=pd.DataFrame({'k1':['a','b','a','a','b','c'],'value':range(6)})
right1=pd.DataFrame({'group_val':[3.5,7]},index=['a','b'])
print(left1)
print(right1)
print(pd.merge(left1,right1,left_on='k1',right_index=True))
### 当列标签名不同时，列中数值有相同且重复时，可以键作为索引，left_index=True, right_index=True 作为第一二参数的的行索引
print(pd.merge(left1,right1,left_on='k1',right_index=True,how='outer')) ## right_index=True:取第二参数的索引即a b，left_on='k1'：取第一参数的列标签k1的内容，['a','b','a','a','b','c']。两者存在重复值，how='outer'：将两者外联接合并，新表索引以第一参数的顺序排序

### 多层索引
a=pd.DataFrame({'k1':['ohio','ohio','ohio','neva','neva'],'k2':[2000,2001,2002,2001,2002],'data':np.arange(5)})
b=pd.DataFrame(np.arange(12).reshape((6,2)),index=[['neva','neva','ohio','ohio','ohio','ohio'],[2001,2000,2000,2000,2001,2002]],columns=['event1','event2'])
print(a)
print(b)
print(pd.merge(a,b,left_on=['k1','k2'],right_index=True))
print(pd.merge(a,b,left_on=['k1','k2'],right_index=True,how='outer'))
#### 用列表的方式指明合并多个列

### 行索引的合并
a=pd.DataFrame([[1,2],[3,4],[5,6]],index=['a','c','e'],columns=['ohio','neva'])
b=pd.DataFrame([[7,8],[9,10],[11,12],[13,14]],index=['b','c','d','e'],columns=['miss','asaf'])
print(a)
print(b)
print(pd.merge(a,b,how='outer',left_index=True,right_index=True)) ## 合并相同行索引，新索引自动从小到大排序
print(a.join(b,how='outer')) # 效果同上，按索引，a中加b，合集

c=pd.DataFrame([[7,8],[9,10],[11,12],[15,16]],index=['a','c','d','e'],columns=['gbk','utf'])
print(a.join([b,c])) # 按照行索引，将b c两表的数据加到a上
print(a.join([b,c],how='outer')) # 合集，

### 沿轴向连接-------拼接、绑定和堆叠 np.concatenate函数
a=np.arange(12).reshape((3,4))
print(np.concatenate([a]*2)) ## 重复2遍列表
print(np.concatenate([a]*2,axis=1)) ## 各个子列表元素2遍

### 连接无相同标签的序列
a=pd.Series([0,1],index=['a','b'])
b=pd.Series([2,3,4],index=['c','d','e'])
c=pd.Series([5,6],index=['f','g'])
print(pd.concat([a,b,c])) # 合并成新序列
print(pd.concat([a,c,b])) # 按先后顺序排列，默认按axis=0
print(pd.concat([a,b,c],axis=1)) ## 输入 忽略，axis=1代表列向
d=pd.concat([a,b]) ## 构造新序列
print(pd.concat([a,d],axis=1)) ## 连接新序列和a序列
print(pd.concat([a,d],axis=1,join='inner')) # 求两个序列的交集
print(pd.concat([a,d],axis=1,join_axes=[['a','c','b']]))
### join_axes=[['a','c','b']]:提取 a d中'a','c','b'标签的值构成新的序列

### 拼接序列的多层索引--------keys值的使用 添加行索引
result=pd.concat([a,b,c],keys=['one','two','three'])
print(result)
print(pd.concat([a,b,c],keys=['one','two','three'],axis=0)) ### 两者效果相同，默认axis=0
print(pd.concat([a,b,c],keys=['one','two','three'],axis=1)) ## 索引发生变化，出现列表名
print(result.unstack()) ## 将行索引转置到列索引

######## DataFrame 中，由于含有行列索引，两者不重复可以相加，重复取交集。由于dateframe是二维数组，一般 axis=1，在series中axis=0/1.
a=pd.DataFrame(np.arange(6).reshape(3,2),index=['a','b','c'],columns=['one','two'])
b=pd.DataFrame(5+np.arange(4).reshape(2,2),index=['a','c'],columns=['three','four'])
print(b) ## 5+np.arange(4).reshape(2,2):从5开始共计4个数
print(pd.concat([a,b],axis=1))
print(pd.concat([a,b],axis=1,keys=['level1','level2']))
print(pd.concat([a,b],axis=0,keys=['level1','level2']))
### 注：axis=1时，行列索引排序有小到大，可重叠相加，keys值即添加标签在列轴向，当axis=0时，keys值添加在行轴上，两个序列行标签机械相加，但列标签排序并非从小到大，这是因为dataframe是二维数组，一般axis=1.
### 当传入对象是字典时，keys值对应字典的键
print(pd.concat({'lev1':a,'lev2':b},axis=1)) #效果同上

## names属性表示生成的层级名称
print(pd.concat([a,b],axis=1,keys=['level1','level2'],names=['upper','lower']))

##### 联合重叠数据---如果两个数据集索引存在部分或者全部重叠，可以将缺失值补齐，创建新的数据集----combine_first，合并缺失值
## series中
a=pd.Series([np.nan,2.4,0.0,3.5,7.8,np.nan],index=['f','a','d','c','b','g'])
b=pd.Series([0.0,np.nan,3.0,9.8,np.nan,8.7],index=['a','b','d','g','c','f'])
print(a.combine_first(b)) ## 将 a b 合并，并把 b中缺失值替换成a中存在的值，新数据集中没有nan

## 同理，在dataframe中，效果一样，如果两个数据集同一个位置均有缺失值，则新数据集中该位置依然是缺失值nan

########  重塑和透视  重排列表格型数据-stack unstack-实质是 series和 dataframe 互变的过程

a=pd.DataFrame(np.arange(6).reshape((2,3)),index=pd.Index(['ohio','color'],name='state'),columns=pd.Index(['one','two','three'],name='number'))
print(a)  ## 注：name：一般接字符串；names：一般接列表
print(a.stack()) ## 将列透视成行。
print(a.stack().unstack()) ## 还原成原数据，行透视成列
print(a.stack().unstack(0)) ## 拆分a.stack().unstack()数据的axis=0 即行索引，将行索引改成列索引
print(a.stack().unstack('state')) ## 效果同上，改变'state'标签即行标签为列标签

#### DataFrame中的复杂调用

a=pd.DataFrame(np.arange(6).reshape((2,3)),index=pd.Index(['ohio','color'],name='state'),columns=pd.Index(['one','two','three'],name='number'))
rel=a.stack()
b=pd.DataFrame({'left':rel,'right':rel+5},columns=pd.Index(['left','right'],name='side'))
print(b) ## 多行标签+列标签
## 传入层级或者层级名称改变序列
print(b.unstack(0)) ## 只将最外层行标签变成列标签
print(b.unstack('state')) ## 效果等同上式。

print(b.unstack('number')) ## 将只第二层行标签变成列
print(b.unstack(1)) ## 效果同上。
print(b.unstack()) ## 效果同上两式
## 两层行标签：（0）：代表最外层；（）/（1）代表第二层

print(b.unstack('state').stack('side')) ## 指明需要堆叠的轴名称。

print(b.stack()) ## 列透视成行，多行标签的series
print(b.stack().unstack('number')) ## 指定相应列成行
print(b.stack().unstack('state').unstack('number'))# 单行多列标签
v=b.stack().unstack('state').unstack('number')
print(v.stack(0)) ## 将最外（最上面）的列标签变成行
print(v.stack(1)) ## 将第二层列标签变成行标签
print(v.stack()) ## 同上（）==（1）两层列标签：（0）：代表最外层；（）/（1）代表第二层


















































