#### ================= 数据的清洗和准备 ===================
import numpy as np
import pandas as pd
from numpy import nan as NA
## 处理缺失值，重复值，字符串等
a=pd.Series(['ab','ac','ag',np.nan,'gh'])
print(a) ## 缺失值记为 NAN
print(a.isnull()) ## isnull：查找哪一个是缺失值
print(a[a.isnull()]) # 返回缺失值
print(a.notnull()) # notnull：找哪一个不是缺失值
print(a[a.notnull()]) #返回不是缺失值的行与值

## dropna 等价 a.notnull() ：返回非缺失值的所有数据，根据标签对应值是否是缺失值来查找缺失值

## DateFrame 中，dropna 默认删除所有含有NA 的行列
a=pd.DataFrame([[1,2,3],[1,NA,NA],[NA,NA,NA],[NA,6.5,5.]])
print(a.dropna()) ## 留下不含NA 的行
print(a.dropna(how='all',axis=0)) # 只删除所有行为NA，返回剩下数据
a[4]=NA
print(a.dropna(how='all',axis=1)) # 只删除所有列为NA的数据

## thresh函数，保留一定数量的NA的行，部分行有NA
a=pd.DataFrame(np.random.randn(7,3),columns=['a','b','c'])
print(a)
a.iloc[:3,1]=NA  ##切片赋值
a.iloc[:2,2]=NA
print(a)
print(a.dropna()) # 保留不含NA的数据
print(a.dropna(thresh=2)) # 从数组第3行开始，保留含有NA的列

## 补全缺失值 --------- fillna
a=pd.DataFrame(np.random.randn(7,3),columns=['a','b','c'])
a.iloc[:3,1]=NA  ##切片赋值
a.iloc[:2,2]=NA
print(a.fillna(0)) ## 一般用常数0代替NA
## 调用字典，为不同列设定不同填充值
print(a.fillna({'b':1.0,'c':2.})) #根据不同列标签调用字典
## fillna返回新对象，也可改变源对象，在调用时。则原数据已发生变化。
_=a.fillna(0,inplace=True) # 原数据以改变
print(a)

b=pd.DataFrame(np.random.randn(8,4),columns=['a','b','c','d'])
b.iloc[2:,1]=NA
b.iloc[4:,2]=NA
print(b)
print(b.fillna(method='ffill')) # 每一列将NA填充为离NA最近的数值
print(b.fillna(method='ffill',limit=3)) #limit：用于向前或者向后填充的最大范围，本例子，向下将NA填充为数据最大范围为3剩下的任为NA
a=pd.Series([1,2,NA,55,NA,84])
print(a.fillna(a.mean())) ## 将NA填充为该列数据的平均数

### 数据转换
# 删除重复值 删行，去列
a=pd.DataFrame({'k1':['one','two']*3+['two'],'k2':[1,1,2,3,3,4,4]})
print(a) ## 字典形式
print(a.duplicated()) #duplicated()：判断是否出现重复行，与上一行
print(a.drop_duplicates()) # 返回的是除了重复行剩下部分

a['v']=range(7) # 添加一列
print(a)
print(a.drop_duplicates(['k2'])) # 去除一列重复值，第二个数值去除
## drop_duplicates 和 duplicates 都是保留第一个重复值，传入参数keep='last' 将会保留后一个
print(a.drop_duplicates(['k2'],keep='last'))
print(a.drop_duplicates(['k2','k1'])) ## 删除两列共同的重复值

## 替代值 replace
a=pd.Series([1,4,-99,3,-777])
print(a.replace(-99,88)) ## 后者替代前者
print(a.replace([-99,-777],np.nan)) # 替代多个值
print(a.replace([-99,-777],[0,np.nan])) # 对应替代
print(a.replace({-99:np.nan,1:10000})) #字典型替代

### 重命名轴索引
## 函数映射------map函数
# map() 会根据提供的函数对指定序列做映射 map(function, iterable, ...) 将后面序列值调入函数中输出一个列表或者元组等类型的值func = lambda  x:x+2 result = map(func, [1, 2, 3, 4, 5] # print(list(ruslt)) [3,4,5,6,7]

## seriesz中的map方法可以接受一个函数或者映射关系的字典对象，如：str.lower()：将每个字符串大写改为小写,str.upper():相反。
a=pd.DataFrame({'food':['Bacon','Pastrmi','Apple'],'ounces':[4,5,9]})
print(a)
meat_to_animal={'bacon':'pig','pastrmi':'cow','apple':'salmon'} ## 新建一个字典
b=a['food'].str.lower() ## 将food列改为小写字母
print(b)
a['animal']=b.map(meat_to_animal) ##将新建字典传入a表中并且位于'animal'列标签下 ，map 无函数时具有传入功能，注意b字典的键要和meat_to_animal字典的键类型一致，否则无法映射
print(a)

## 轴索引的map映射法 map函数映射函数
a=pd.DataFrame(np.arange(12).reshape((3,4)),index=['Ohio','Colo','Newyork'],columns=['one','two','three','four'])
print(a)
t=lambda x:x[:4].upper() # 注：切片索引，前四个字母大写，[:4],只表示行标签索引，[:4,:2]：表示行列切片
print(a.index.map(t)) # 输出映射后的索引
a.index=a.index.map(t) ## 将索引重新赋值
print(a)
print(a.columns.map(t)) ## 同理可以改变列标签字符串
a.columns=a.columns.map(t) ## 将列标签改大小写
print(a)
## rename 函数也可以改标签，但不修改原数据，一般结合字典
a=pd.DataFrame(np.arange(12).reshape((3,4)),index=['Ohio','Colo','Newyork'],columns=['one','two','three','four'])
b=a.rename(index={'Ohio':'INDF'},columns={'three':'book'})
print(b) ## 用字典重命名法替换行列标签
print(a) # 原数据不变
a.rename(index={'Ohio':'INDF'},columns={'three':'book'},inplace=True) ## 改变原数据 inplace=True
print(a) ## 原数据改变

#### 离散化和分箱 pd.cut函数
ages=[20,22,25,27,21,23,37,31,61,45,41,32]
bins=[18,25,35,60,100] # 分段 4区间
cats=pd.cut(ages,bins) # 返回的是特殊对象，一组开闭和区间的数组，共分成12个箱，对应age中的12个年龄
print(cats)
print(cats.codes) # age的数据标签
print(cats.categories) ## 一列不重复的年龄段，小括号是开放即不包括边，中括号是封闭即包括边。可以通过 right=Flase改变哪一边的封闭情况。
print(pd.cut(ages,bins,right=False)) # 右边不包括
print(pd.value_counts(pd.cut(ages,bins))) # 计数各年龄段的人次pd.value_counts.
## 通过labels选项改变箱名，传入一个数组或者列表
group_names=['ab','ac','an','ag']
print(pd.cut(ages,bins,labels=group_names))

### 均匀分箱
a=np.random.randn(30) ## 随机30个数，均分成5段，每个数保留3位小数
print(pd.cut(a,5,precision=3))

## 检测与过滤异常值

### 字符串的操作
a='a,bn,    ehk'
print(a.split(',')) # split函数根据标记分开字符串，结果有空格
### split（分开字符）+strip（清除空格）：可以清除空格和换行
b=[x.strip() for x in a.split(',')] # x 代表每一个字符串
print(b)
#abc,dg,hj=b ## 将 b 中的三个字符串分别赋值给三个变量
print('::'.join(b)) ## 通过::符号 join函数连接起来
print('--'.join(b)) ## 同上

### 定位子字符串  in ， find
print('ehk' in a) ## 查找 子字符串是否在母字符串中，返回布尔值
print(a.find('bn')) ## 返回第一次找到子字符串的位置，非数组位置
print(a.find(':')) ## 没有返回-1
print(a.count(','))## 返回某一种字符串出现次数
print(a.replace(',','::')) ## 用一种模式代替另一种模式
print(a.replace('::','')) ## 用空字符串模式代替原模式
print(a.strip()) ## 效果同上

#### 正则表达式 re模块，模式匹配，替代，拆分
import re
a="foo    nb\t bac  \ty"
print(re.split('\s+', a)) ## 返回删除空格和换行符后的列表 \s+
## 创建一个正则对象作用多个字符串上 re.compile 自行编译
b=re.compile('\s+')
print(b.split(a)) # 效果同上

























