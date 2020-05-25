import numpy as np
import pandas as pd
from numpy import nan as NA
import warnings
warnings.filterwarnings("ignore")

#####=====================  时间序列  =====================
from datetime import datetime
print(datetime.now())
print(datetime.now().year)
print(datetime.now().day)

#### 时间差-----timedelta datatime 存储时间和日期
delta=datetime(2019,10,15)-datetime(2010,9,3,6,24) # 年月日时分
print(delta)
print(delta.days)
print(delta.seconds)

from datetime import timedelta
start=datetime(2018,4,6)
print(start+timedelta(19)) ## 6+19=25
print(start-2*timedelta(11)) # 从2018-4-6往前倒22天

### 字符串与datetime互相转换-----日期.strftime('格式')
time=datetime(2019,2,15,5,6)
print(str(time))
print(time.strftime('%y-%m-%d')) ## y:两位年份
print(time.strftime('%Y-%m-%d')) ## Y:四位年份

#### datatime.srtptime('日期'，'格式') 两者形式一致,适用于已经日期格式的情况下
print(datetime.strptime('2010-4-28','%Y-%m-%d'))
print(datetime.strptime('2010,4,28','%Y,%m,%d'))

datestrs=['7/8/2017','9/11/2018']
print(datetime.strptime(x,'%m/%d/%Y') for x in datestrs)
### 输出值为对象
print([datetime.strptime(x,'%m/%d/%Y') for x in datestrs])

#### 安装第三方包 dateutill parser.parse
from dateutil.parser import parse
print(parse('2019-07-09'))
print(parse('2019/07/09'))
print(parse('2019,Jan,16'))

### 国际场合下，日月年的表达。需要传递dayfirst=true
print(parse('6/12/2018',dayfirst=True))

### to_datetime处理缺失值（None 空字符串）
datestrs=['7/9/2017','9/11/2015']
print(pd.to_datetime(datestrs))
print(datestrs[1])
i=pd.to_datetime(datestrs+[None])  ## 添加一个缺失值
print(i)
print(i[2])
print(pd.isnull(i)) ## 判断是否是 null（缺失值）

###### 时间序列基础
datas=[datetime(2011,1,1),datetime(2012,3,4),datetime(2014,5,6),datetime(2015,5,8),datetime(2016,9,5),datetime(2020,1,1)]
a=pd.Series(np.random.randn(6),index=datas)
print(a)
print(a.index)  ### 将行索引存入datetimeindex中
print(a[:2])
print(a[::2])
print(a+a[::2]) ### 以上均是数组切片，相同时间标签对应值运算

### 索引，选择，子集
b=a.index[2] ## 输出行索引
print(b)
print(a[b])  ## 输出索引对应值
print(a['20110101'])
print(a['09/05/2016']) ## 输出可以解释的日期字符串

#### 长时间的序列，可以通过年月日对其进行数据切片，pd.date_range（）：时间排序函数
long_times=pd.Series(np.random.randn(1000),index=pd.date_range('1/1/2010',periods=1000))
print(long_times) ## 提取 1/1/2010 到2012-09-26共计1000天数据
print(long_times['2011']) ## 提取 2011年的时间及数据
print(long_times['2012-08'])  ## 提取 2012-08月份的时间
print(long_times[datetime(2010,10,9):]) ## 数组切片
print(long_times['2010-09-11':'2011-03-19'])  ## 特定区间内数组切片提取数据
print(long_times[datetime(2011,1,3):]) ## 注：datetime(2011,1,3)该时间不在原时间序列内，但也可以切片或提取特定时间区间，从该时间点截取往后1000天数据。
print(a.truncate(after='1/9/2012')) ## ????

### 含有重复索引的序列
a=['1/3/2010']*3+['1/5/2010']+['4/6/2010']
b=pd.Series(np.random.randn(5),index=a)
print(b)
print(b.index.is_unique) ## 判断索引逻辑值是否唯一
print(b['1/3/2010']) ## 重复。多组数据
print(b['1/5/2010']) ## 不重复

#### 传递 groupby的level=0，可以使想聚合含有唯一时间戳的数据
print(b.groupby(level=0).mean())
print(b.groupby(level=0).count())  ## 表名重复值个数

#### 日期范围，频率和移位

























