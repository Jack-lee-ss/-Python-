##================ 数据聚合与分组的操作 ==================
import numpy as np
import pandas as pd
from numpy import nan as NA
import warnings
warnings.filterwarnings("ignore")

### GroupBy 机制--- 拆分，应用，联合（以数组或者列表分开）
##  分组键：按照什么方式将数据集分开。可以是和需要分组的轴长度一致的值列表和值数组，DataFrame列标签，相匹配的字典或者Series，单个标签下调用的函数
a=pd.DataFrame({'k1':['a','a','b','b','a'],'k2':['one','two','one','two','one'],'data1':np.random.randn(5),'data2':np.random.randn(5)})
print(a)
print(a['data1'].groupby(a['k1'])) ## 输出的是groupby的对象，非数值，占用内存位置。这里a['k1']是值列表，即分组键。但是对a['data1']列数据没有进行运算或者其他操作，所以没有数值的返回值，只是返回了对象和其子内存的大小位置。
print(a['data1'].groupby(a['k1']).mean()) ## .groupby(a['k1'])：对该列先分组，相应的a['data1']也被分组，.mean()对相应组求均值。
print(a['data1'].groupby([a['k1'],a['k2']]).mean())
## 传入多列数，注意：使用列表方式括起，两个一维数组形式，只对一列运算
print(a.groupby([a['k1'],a['k2']]).mean())#当不表明哪一列时默认所有有数据列都参加运算。
print(a.groupby(['k1','k2']).mean()) ## 效果同上，两种写法

print(a.groupby('k1').mean()) ## 当单一值列表时可以写成('k1')，多个值列表要写成 [a['k1'],a['k2']]/['k1','k2']

## 分组键是相应长度的任何数组时
states=np.array(['ohio','cal','cal','ohio','ohio'])
years=np.array([2003,2005,2006,2005,2006])
print(a.groupby([states,years]).mean()) ## 按.groupby([states,years])分组，一般都是分成含有行索引的形式.注意：数组形式，可以写成 [states,years] 区别 值列表 a['k1']
print(a.groupby([states,years]).mean().unstack(0)) ## 在拆堆

## size 用法 返回一个包含组大小信息的 series
print(a.groupby(['k1','k2']).size())

### 遍历各分组----生成一个包含组名和数据块的2维元组序列
for name,group in a.groupby('k1'):
	print(name)
	print(group)
## 提取并将'k1'列中 a b 分组，在将对应数据整合一起
for name,group in a.groupby(['k1','k2']):
	print(name)
	print(group)
## 提取并分组同时符合['k1','k2']相应数值的序列

### 当多个分组键的情况下，元组中的第一个元素是键值的元组
for (k1,k2),group in a.groupby(['k1','k2']):
	print((k1,k2))
	print(group)
## 效果同上

### 通过字典选取任意的一块数据，提取需要的分组过的数据集，不需要遍历
pieces=dict(list(a.groupby('k1')))
print(pieces['a']) ## 只提取 'a'的数值
print(dict(list(a.groupby('k1')))['b']) ## 只提取 'b' 的数值

## 默认情况下，groupby 在axis=0轴上分组，但可以在任意轴向分组
print(a.dtypes) ## 对 a 数据集根据不同属性进行分组
grouped=a.groupby(a.dtypes,axis=1)
for dtype,group in grouped:
	print(dtype)
	print(group)

### 选择一列或者所有列的子集-----语法糖
print(a.groupby('k1')[['data2']].mean()) ## 无数据形式
print(a.groupby('k1')['data2'].mean())
print(a['data2'].groupby(a['k1']).mean()) ## 同上，含有数据形式

### 使用字典和Series分组
a=pd.DataFrame(np.random.randn(5,5),columns=['a','b','c','d','e'],index=['joe','bob','tom','jim','alia'])
a.iloc[2:3,[1,2]]=np.nan ## 添加缺失值，一个切片+2个值的数组
print(a)
mapping={'a':'red','b':'red','c':'blue','d':'blue','e':'black','f':'orange'} ## 多写了f
b=a.groupby(mapping,axis=1) ## 引入字典，将分列分组对应关系累加或者求平均数。
print(b.mean())
print(b.sum())

c=pd.Series(mapping) ## 将 字典表示成series形式
print(c)
print(a.groupby(c,axis=1).count()) ## 按列轴标签名分组，并且计数，

####### 使用函数分组---不同功能的函数名作为分组键
print(a.groupby(len).sum()) ### 默认axis=0
k_list=['one','one','one','two','two']
print(a.groupby([len,k_list]).min()) ## 混合函数，列表，同时满足[len,k_list]的数据的最小值

### 分层索引分组
a=pd.MultiIndex.from_arrays([['us','us','us','jp','jp'],[1,3,5,1,3]],names=['city','tenor'])
b=pd.DataFrame(np.random.randn(4,5),columns=a)
print(b)
print(b.groupby(level='city',axis=1).count())
### 将层级数值或者名称传给level关键字作为分组键

### 数据聚合---数据产生标量值的数据转换过程
## 逐列及多函数应用
tips=pd.read_csv('D:/data/tips.csv') ## 读取文件
print(tips[:6])
tips['tip_pct']=tips['tip']/tips['total_bill'] ## 添加一列
print(tips[:6])
### agg函数：聚合函数，分别聚合一系列数据,根据一定的对应关系连接数据

grouped=tips.groupby(['day','smoker']) # 根据['day','smoker']对tips分组。
print(grouped['tip_pct'].agg('mean'))
print(tips.groupby(['day','smoker'])['tip_pct'].agg('mean'))  #### 同上效果。注意：单个数值列用中括号['tip_pct']
print(tips['tip_pct'].groupby([tips['day'],tips['smoker']]).agg('mean'))  ## 同上

print(tips.groupby(['day','smoker'])['tip_pct'].agg(['mean','std'])) ### 传递的函数名如果是自带的优化函数，要加单引号，自定义函数则不需要，传递多个函数则会得到一个dataframe。可以更改以函数名命名的列标签，可以引用二元元组的列表（name,function）是对应值。
print(tips.groupby(['day','smoker'])['tip_pct'].agg([('均值','mean'),('标准差','std')]))  ## 二元元组引用

##### 如果要对任一列使用不同函数时，先创建优化函数或者自定义列表
functions=['count','mean','std']
print(tips.groupby(['day','smoker'])['tip_pct','total_bill'].agg(functions))

print(tips.groupby(['day','smoker'])['tip_pct','total_bill'].agg(functions)['total_bill']) ## 可以单独提取其中一列
print(tips.groupby(['day','smoker'])['total_bill'].agg(functions)) ## 同上

#### 可以传递二元元组更改列标签的函数名
ftup=[('总计','count'),('均值','mean'),('标准差','std')]
print(tips.groupby(['day','smoker'])['tip_pct','total_bill'].agg(ftup))

#### 将不同函数应用到一列或者多列上----字典对应引用关系
print(tips.groupby(['day','smoker']).agg({'tip':np.max,'size':'sum'}))
print(tips.groupby(['day','smoker']).agg({'tip':[np.max,'min','max','mean','std','var'],'size':'sum'}))

#### 返回不含行索引的聚合数据---as_index=False
print(tips.groupby(['day','smoker']).mean())
print(tips.groupby(['day','smoker'],as_index=False).mean())


########### 拆分----应用------联合
print(tips.groupby(['day','smoker'])['tip_pct'].describe())
print(tips.groupby(['day','smoker'])['tip_pct'].describe().unstack('smoker'))

#### 压缩分组键-----传入group_keys=False

###  分位数与桶分析---cut/qcut:将数据按照选择的箱位或样本分位数分桶
a=pd.DataFrame({'data1':np.random.randn(1000),'data2':np.random.randn(1000)})
b=pd.cut(a.data1,4)  ### 均分成4块
print(b[:10])
#### cut返回一个categorical类型对象，可以直接传给groupby，我们可以在生成的4个区间统计data2中的数据集，
def fun(i):
	return {'min':i.min(),'max':i.max(),'count':i.count(),'mean':i.mean()}
print(a.data2.groupby(b).apply(fun))
print(a.data2.groupby(b).apply(fun).unstack()) ## 获得区间统计值 等长桶，即区间大小相等，但里面数据个数不等

c=pd.qcut(a.data1,4,labels=False)
print(a.data2.groupby(c).apply(fun))
print(a.data2.groupby(c).apply(fun).unstack())
### 等大小桶，区间内数据个数相等

########## 实例展示
##### 使用指定分组值填充缺失值---清除缺失值时一般用dropna,但有时需要通过修正值或者其他数据填充缺失值NA，可以用fillna。填充值是常量
a=pd.Series(np.random.randn(10))
a[::3]=np.nan ### 将缺失值每隔3位替换随机数
print(a)
print(a.fillna(a.mean())) ## 用平均值代替缺失值

## 如果填充值按组发生变化-----填充值是变化的
a=['ohio','over','khjg','dfhue','lgo','beijing','sjagnh','anshdi']
b=['east']*4+['west']*4 #### 列表可以运算，会生成一个总列表包含子元素。
##print(b)
f=['erer'*5+'ob'*4] ### 列表里的字符串也可以运算，直接相连
##print(f)
data=pd.Series(np.random.randn(8),index=a)
data['ohio','beijing','anshdi']=np.nan  ## 设为缺失值
print(data)
print(data.groupby(b).mean()) ## 引用的 b 列表分为两类，east 对应 a 列表中前4个数值，west对应 a 列表中后4个数值。

##### 使用分组后的两类数据。即west和east的平均值填充到各自缺失值中，取代了将整体的平均值替换局部缺失值的做法，使数据更合理





####### 分组加权平均和相关性
#在Numpy中， mean() 和 average(）都有取平均数的意思，在不考虑加权平均的前提下，两者的输出是一样的.考虑权重的情况下， average() 还可以计算一维的加权平均值
a = np.array([1,2,3,4])

w = np.array([4,3,2,1])

print( np.average(a, weights=w))
# 那么这个2.0是怎么得到的， 具体的加权平均是怎么计算的，解析如下：np.average(a, weights=w) =  a[0] * w[0] / w.sum()  +
#
#                                               a[1] * w[1] / w.sum()  +
#
#                                               a[2] * w[2] / w.sum()  +
#
#                                               a[3] * w[3] / w.sum()
#
# w.sum() = w[0] + w[1] + w[2] + w[3[ = 10
#
# np.average(a, weights=w) = 1 * 4 / 10 + 2* 3 / 10 + 3* 2/ 10 + 4* 1 / 10 = 0.4 + 0.6 + 0.6 + 0.4  = 2.0

a=pd.DataFrame({'category':['a']*4+['b']*4,'data':np.random.randn(8),'weig':np.random.randn(8)})
print(a)
grouped=a.groupby('category')
b=lambda i:np.average(i['data'],weights=i['weig'])
print(grouped.apply(b))









