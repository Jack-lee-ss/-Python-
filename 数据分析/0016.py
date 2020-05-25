import matplotlib.pyplot as plt
import numpy as np
import random
import seaborn
import pandas as pd
import seaborn as sns
import scipy.stats as sci
## 不发出并且忽略警告
import warnings

from numpy import median

warnings.filterwarnings('ignore')
## 设置中文字体
from  matplotlib import font_manager
my_font=font_manager.FontProperties(fname="C:/Windows/fonts/msyhbd.ttc")
tips=pd.read_csv(r'D:/data/pydata-book-2nd-edition/examples/tips.csv')

####  分类变量-----分类散点图
## 一般散点图 scatterplot()
# sns.set_style('whitegrid')
# sns.set_context('paper')
# sns.scatterplot(x='total_bill',y='day',data=tips)
# ## 效果重叠
# plt.show()
#
# ### 引入随机抖动---在水平或者竖直方向将数据展开，避免重叠
# ## stripplot()
# sns.stripplot(x='total_bill',y='day',data=tips)
# plt.show()
#
# ## 通过jitter指定抖动宽度，交换xy改变图的方向,加大抖动宽度
# sns.stripplot(x='total_bill',y='day',data=tips,jitter=0.3)
# plt.show()
#
# ### 用不同颜色区分吸烟与不吸烟（第三变量，有两种水平，吸烟与不吸烟），参数dodge使第三变量散点分离。dodge=True
# sns.stripplot(x='total_bill',y='day',hue='smoker',data=tips,jitter=0.2,dodge=True,palette='autumn',size=15,marker='d',edgecolor='gray',alpha=0.25)
# plt.show()
# ### 不分离 dodge=False
# sns.stripplot(x='total_bill',y='day',hue='smoker',data=tips,jitter=0.2,dodge=False,palette='autumn',size=15,marker='d',edgecolor='gray',alpha=0.25)
# plt.show()
#
# ### 将随机抖动沿水平展开--------swarmplot散点图
# sns.swarmplot(x='total_bill',y='day',data=tips,hue='smoker')
# plt.show()
#
# sns.swarmplot(x='time',y='tip',data=tips,palette='summer',hue='smoker')
# plt.show()
#
# ###########  散点图一般针对数据少时采用，过多时，点密集，不易观察。一般散点图作为辅助特效。
# sns.violinplot(x='day',y='total_bill',data=tips,palette='cool',inner=None)
# sns.swarmplot(x='day',y='total_bill',data=tips,palette='winter',edgecolor='white',alpha=0.5)
# plt.show()
#
# sns.violinplot(x='day',y='total_bill',data=tips,palette='cool',inner=None)
# sns.swarmplot(x='day',y='total_bill',data=tips,hue='smoker',palette='spring',edgecolor='white',alpha=0.5)
# plt.show()
#
# ##########  分类变量-----条形图barplot(),展示离散变量集中趋势
# ## 统计每天是否是 smoker 的人数
# sns.set_style('white')
# sns.countplot(x='day',hue='smoker',palette='Set2',data=tips)
# plt.show()

#### 不同日期下消费统计量展示，默认显示均值和95%置信区间
# sns.barplot(x='day',y='tip',hue='smoker',palette='Set2',data=tips)
# plt.show()
#
# ### 显示均值的标准误差 ci=68: 68%的置信区间
# sns.barplot(x='day',y='tip',palette='Set2',data=tips,ci=78)
# plt.show()
#
# ## 中位数取代均值 导入 estimator= median  from numpy import median
# sns.barplot(x='day', y='tip', palette='Set2', data=tips, estimator=median)
# plt.show()
#
# ### 估计总和 estimator=sum
# sns.barplot(x='day', y='tip', palette='Set2', data=tips, estimator=sum)
# plt.show()
#
# ### 增加新的分类变量 hue=smoker
# sns.barplot(x='day', y='tip', palette='Set2', data=tips, estimator=sum,hue='smoker')
# plt.show()

#######  点图 pointplot()
# plt.subplot(1,2,1)
# sns.barplot(x='size',y='tip',palette='Blues',data=tips)
# plt.subplot(1,2,2)
# sns.pointplot(x='size',y='tip',data=tips)
# plt.show()

### 添加变量
# sns.pointplot(x='size',y='tip',data=tips,hue='smoker')
# ## 用餐者增多，不吸烟小费增多
# plt.show()

#### 估计值改为sum
# plt.subplot(2,1,1)
# sns.barplot(x='size',y='tip',data=tips,hue='smoker',palette='Blues')
# plt.subplot(2,1,2)
# sns.pointplot(x='size',y='tip',data=tips,hue='smoker')
# plt.show()

###### 箱线图:非常适合比较不同类的数据-----boxplot()
# i=np.random.normal(0,1,1000)
# sns.boxplot(i)
# plt.show()

### 比较数据形状  tips
# sns.boxplot(x='day',y='tip',data=tips,palette='Set2')
# plt.show()

### 添加变量 hue=sex
# sns.boxplot(x='day',y='tip',data=tips,palette='Set2',hue='sex')
# plt.show()

########## 小提琴图：结合了核密度图+箱线图，更好展示多峰分布，但不显示异常值。可能产生误导。
# sns.violinplot(x='day',y='tip',data=tips,palette='Set2',hue='smoker')
# plt.show()

### 内部设置
##  scale=count:宽度按该箱中观察次数缩放，数据多则宽，少则扁；scale=width:宽度相同。
##  split=True:更容易直接比较分布。
##  inner={box, quartile, point, stick, None}默认是 box.表示图形内部数据点。box:绘制微型箱图；quartile:绘制四分位数；point/stick:显示每个数据点；None:使用kde
# sns.violinplot(x='day',y='tip',data=tips,palette='Set2',hue='sex',split=True,scale='count',inner='stick')
# plt.show()

# sns.violinplot(x='day',y='tip',data=tips,palette='Set2',hue='sex',split=True,scale='count',inner='quartile')
# plt.show()

#### 分类变量 ---大量数据boxplot-Boxen
## 小数据集（n<200），四分位以外的尾部不显示或者不精确，异常值数量小于10,；大数据（n>10000）,boxplot对四分位以外的数据尾部精确估计。
## 四分位数：在统计学中把所有数值由小到大排列并分成四等份，处于三个分割点位置的数值。在25%位置上的数值（称为下四分位数）和处在75%位置上的数值（称为上四分位数）
## violion()也可以增强尾部，需要用高斯核，但依赖特殊的估计kde，无法体现均匀分布。还需要增加平滑参数（带宽），由于kde和带宽不同，效果不同，但 boxen 不会出现。
# 产生正太分布
# v1=np.random.normal(0,1,9000)
# # 产生符合均分布的浮点数
# v2=np.random.uniform(5,6,1000)
# # 链接一起
# v=np.append(v1,v2)
# plt.subplot(2,2,1)
# sns.distplot(v,kde=False,bins=10)
# # 默认带宽
# plt.subplot(2,2,2)
# sns.violinplot(v)
# plt.subplot(2,2,3)
# sns.boxenplot(v)
# plt.subplot(2,2,4)
# # 设置带宽
# sns.violinplot(v,bw=0.02)
# plt.show()

#### tips天数变化在smoker下boxen的对比
# plt.subplot(2,1,1)
# sns.boxplot(x='day',y='tip',data=tips,palette='Set2',hue='smoker')
# plt.subplot(2,1,2)
# sns.boxenplot(x='day',y='tip',data=tips,palette='Set2',hue='smoker')
# plt.show()


#### Categorical数据类型-catplot：可以引用多个轴级功能（分类散点，分布，估计图）改变参数kind=不同属性，即可调用不同属性的图形类型。
# sns.catplot(x='day',y='tip',data=tips,hue='smoker',palette='Set3',kind='strip')
# plt.show()
# sns.catplot(x='day',y='tip',data=tips,hue='smoker',palette='Set3',kind='box')
# plt.show()
# sns.catplot(x='day',y='tip',data=tips,hue='smoker',palette='Set3',kind='swarm')
# plt.show()
# sns.catplot(x='day',y='tip',data=tips,hue='smoker',palette='Set3',kind='boxen')
# plt.show()
# sns.catplot(x='day',y='tip',data=tips,hue='smoker',palette='Set3',kind='violin')
# plt.show()
# sns.catplot(x='day',y='tip',data=tips,hue='smoker',palette='Set3',kind='bar')
# plt.show()
# sns.catplot(x=None,y='tip',data=tips,hue='smoker',palette='Set3',kind='count')
# plt.show()

#### 结构化绘制网格-----重叠密度（FacetGrid）https://blog.csdn.net/Droke_Zhou/article/details/87744702
### 提供多图网格，将绘图结构连接到数据集上，FacetGrid可以在三个维度上绘制：row,col,hue,Axes的行和列为两个维度，色调关系是第三个维度，不同的子集使用不同的颜色来绘制。
## 初始化网格
#a=sns.FacetGrid(tips,col='time')
#plt.show()
## 在建立的网格上绘制直方图
# col='time':表示从数据集‘time’列的方向看，
# a=sns.FacetGrid(tips,col='time')
# # map():映射到具体的 seaborn 图表类型
# a.map(plt.hist,'tip')
# plt.show()
#
# ## 添加图例
# b=sns.FacetGrid(tips,col='time',hue='smoker')
# # map():不添加 'x=';'y='
# b.map(plt.scatter,'total_bill','tip',alpha=0.5)
# b.add_legend()
# plt.show()


#### 极坐标投影
# r=np.linspace(0,10,num=100)
# df=pd.DataFrame({'r':r,'slow':r,'medium':2*r,'fast':4*r})
# print(df.head())

## 将DataFrame从long-form变成整洁的形式
## pd.melt():将列名转换为列数据，重构DataFrame
## id_vars:不需要被转换的列名。
## value_vars:需要转换的列名，如果剩下的列全部都要转换，就不用写了
## var_name和value_name是自定义设置对应列名。
# df=pd.melt(df,id_vars=['r'],var_name='speed',value_name='theta')
# print(df.head())

### 设置具有极坐标的投影的轴网格
## 生成高度为6的极坐标，彼此不共享坐标轴，图脊关闭。
# s=sns.FacetGrid(df,col='speed',hue='speed',subplot_kws=dict(projection='polar'),height=6,sharex=False,sharey=False,despine=False)
# s.map(sns.scatterplot,'theta','r')
# plt.show()


### 热力图
## 自带数据集
# a=sns.load_dataset('flights')
# print(a.head())
# ## 转化为长格式
# a=a.pivot('month','year','passengers')
# print(a.head())
# ## annot: 默认为False，为True的话，会在格子上显示数字; fmt，字符格式设置 整数，浮点数。。。
# sns.heatmap(a,annot=True,fmt='d',linewidths=1)
# plt.show()

##### 风格细节设置
## 原图
# def sinplot(flip=1):
# 	x=np.linspace(0,14,100)
# 	for i in range(1,7):
# 		plt.plot(x,np.sin(x+i*0.5)*(7-i)*flip)
# sns.set(style='white')
# sinplot()
# plt.show()
#
# sinplot()
# ## 去除图脊
# sns.despine()
# plt.show()
#
# ## 去除图脊增加轴间距
# sinplot()
# sns.despine(offset=50,left=True)
# plt.show()
#
# ## 当刻度不覆盖轴的整个范围时，限制轴的显示范围
# sns.violinplot(x='size',y='tip',data=tips,palette='Set3')
# sns.despine(offset=10,trim=True)
# plt.show()
#
# ### 暂时设定图的样式
# f=plt.figure(figsize=(12,6))
# with sns.axes_style('darkgrid'):
# 	f.add_subplot(1,2,1)
# 	sinplot()
# f.add_subplot(1,2,2)
# sinplot()
# plt.show()
#
# ## set_context()：调用参数，font_scale:缩放字体大小
# sns.set_context('notebook',font_scale=1.5,rc={'lines.linewidth':2.5})
# sinplot()
# plt.show()
#
# ## 配置背景颜色亮度
# sns.set_style('darkgrid',{"axes.facecolor":"0.4"})
# sinplot()
# plt.show()

#### 调色板设置
## 默认调色板：deep,muted,pastel,bright,dark和colorbind,变深，浅，亮。。。
# current_palette=sns.color_palette()
# sns.palplot(current_palette)
# plt.show()
#
# ### 调入不同颜色
# current_palette=sns.color_palette('deep')
# sns.palplot(current_palette)
# plt.show()
#
# ## 更改原曲线的默认色板
# def sinplot(flip=1):
# 	x=np.linspace(0,14,100)
# 	for i in range(1,7):
# 		plt.plot(x,np.sin(x+i*0.5)*(7-i)*flip)
# sns.set(style='white')
# sinplot()
# plt.show()
# ## 更改色板
# with sns.color_palette('PuBuGn_d'):
# 	sinplot()
# 	plt.show()

### cubehelix_palette()函数的连续调色板
## 一些时候以灰色打印但不降低灰度
pal=sns.cubehelix_palette(n_colors=10,start=0,rot=0.1,light=0.7)
sns.palplot(pal)
plt.show()

## 更改旋转速度 rot=0.5，得到另一些调色板
pal=sns.cubehelix_palette(n_colors=10,start=0,rot=0.5,light=0.7)
sns.palplot(pal)
plt.show()

### 生成离散型调色板 diverging_palette
pal=sns.diverging_palette(h_neg=250,h_pos=10,n=10)
sns.palplot(pal)
plt.show()



	
















