import inline as inline
import matplotlib.pyplot as plt
import numpy as np
import random
import seaborn
import matplotlib
import pandas as pd
import seaborn as sns
import scipy.stats as sci
import warnings
from  matplotlib import font_manager
my_font=font_manager.FontProperties(fname="C:/Windows/fonts/msyhbd.ttc")
tips=pd.read_csv(r'D:/data/pydata-book-2nd-edition/examples/tips.csv')
# x=tips['tip']
# sns.set(context="notebook", style="darkgrid", palette="deep",font="sans-serif", font_scale=1, color_codes=True, rc=None) 默认值，如果显示默认值，图片无颜色填充，单调。
# sns.set()
# 出现正太曲线
# sns.distplot(x)
# plt.show()
# # 禁用曲线
# sns.distplot(x,kde=False)
# plt.show()
#
# # 设置不同颜色网格
# # 白色网格
# sns.set(style='whitegrid')
# sns.distplot(x,kde=False)
# plt.show()
# # 黑色网格
# sns.set(style='darkgrid')
# sns.distplot(x,kde=False)
# plt.show()
# # 去掉网格,背景填充黑色
# sns.set(style='dark')
# sns.distplot(x,kde=False)
# plt.show()
# # 去网格，添白色
# sns.set(style='white')
# sns.distplot(x,kde=False)
# plt.show()
# # 增加坐标轴
# sns.set(style='ticks')
# sns.distplot(x,kde=False)
# plt.show()

# 绘制散点图
# sns.scatterplot(x='total_bill',y='tip',hue='day',style='time',sizes=(20,200),data=tips)
# plt.show()
# sns.scatterplot(x='total_bill',y='tip',hue='size',size='size',sizes=(20,200),data=tips,palette='cool')
# plt.show()

## 核密度
sns.set(style='white')
# numpy.random.normal(loc=0,scale=1e-2,size=shape)的意思是一个正态分布,loc(float)：正态分布的均值，对应着这个分布的中心。loc=0说明这一个以Y轴为对称轴的正态分布;scale(float)：正态分布的标准差，对应分布的宽度，scale越大，正态分布的曲线越矮胖，scale越小，曲线越高瘦;size(int 或者整数元组)：输出的值赋在shape里，默认为None.
x1=np.random.normal(0,1,50)
x2=np.random.normal(5,3,50)
# np.append 将一个数组附加到另一个数组的尾部
# x=np.append(x1,x2)
# 生成小棒形式
# sns.rugplot(x,height=0.5,color='r')
# plt.show()

# kedplot 绘制核密度估计值
# shade=True 打开阴影
# sns.kdeplot(x,shade=True,color='b')
# plt.show()
# 阴影下打开带宽 bw
# sns.kdeplot(x,shade=True,color='b',bw=0.05)
# plt.show()
# 无阴影下打开带宽
# sns.kdeplot(x,color='b',bw=0.05)
# plt.show()

# 绘制双变量密度曲线
# 等高线图
# sns.kdeplot(x1,x2)
# plt.show()
# # 等高线填充密度 cmap="Purples_d",cmap：matplotlib的colormap名称或颜色对象；如果没有提供，默认为cubehelix;  map.cbar为TRUE即绘制颜色条; n_levels=30 共30条等高线，密集。
# sns.kdeplot(x1,x2,n_levels=30,cbar=True,cmap="Purples_d")
# plt.show()
# # n_levels=10 共10条等高线，稀疏
# sns.kdeplot(x1,x2,n_levels=10,cbar=True,cmap="Purples_d")
# plt.show()
# # 热力图
# sns.kdeplot(x1,x2,shade=True)
# plt.show()
#
# ## displot 绘制变量分布关系
# x=np.append(x1,x2)
# # 默认开启核密度曲线
# sns.distplot(x,vertical=True)
# plt.show()
# # 更多设置：rug=True,rug_kws={'color':'g'}：开启小棒，参数是绿色；kde_kws={'color':'k',"lw":3,'label':'KDE'}：核密度曲线参数黑色，线宽3，加图例；hist_kws={'histtype':"step","linewidth":3,"alpha":0.5,"color":'g'}：直方图改为只有轮廓的直方图，线宽3，透明度0.5，颜色是绿色。
# sns.distplot(x,rug=True,rug_kws={'color':'g'},kde_kws={'color':'k',"lw":3,'label':'KDE'},hist_kws={'histtype':"step","linewidth":3,"alpha":0.5,"color":'g'})
# plt.show()

## pairplot()函数绘制每一对变量关系。pairplot：特征两两对比
## 传入数据集
DataSet=pd.read_excel(r'D:/data/Iris DataSet.xlsx')
#print(DataSet.head())
# 共4个变量 4×4=16个数据，由于对角线xy数据相等所以是直方图
# data：数据。 g = sns.pairplot(data)
# sns.pairplot(DataSet)
# plt.show()
# diag_kind：关于单变量图（自己与自己比较）的设定，g = sns.pairplot(data, diag_kind="kde") ，单变量为线形图，其他散点
# sns.pairplot(DataSet,diag_kind='kde')
# plt.show()

## hue：根据指定的特征用不同的颜色显示数据，即指定分类标准; palette：用调色板的颜色来画图 Set2 数字越小，颜色越深;注意首字母大写。
# sns.pairplot(DataSet,hue='Species',palette='Set2')
# plt.show()

## 将线性回归模型拟合到散点图, kind：给非单变量图增加画图样式，g = sns.pairplot(data, kind="reg") ，增加 线性回归 kind='reg'
# sns.pairplot(DataSet,kind='reg')
# plt.show()

## 使用不同形状 marker: 用不同的形状每个类别的图像。例如有的是三角，有的是圆点，g = sns.pairplot(data, hue="label", markers=["o", "s", "D"])
# sns.pairplot(DataSet, hue="Species", markers=["o", "s", "d"])
# plt.show()

## 使用点形状，使用参数，使用 edgecolor。plot_kws / diag_kws：可以设置画图的具体参数更改
# sns.pairplot(DataSet, diag_kind="kde", markers="+",plot_kws=dict(s=50, edgecolor="b", linewidth=1),diag_kws=dict(shade=True))
# plt.show()

## vars：只留几个特征两两比较
# sns.pairplot(DataSet, vars=["Sepal length", "Sepal width"])
# plt.show()


### 线性回归两个常用函数(regplot(),lmplot())---------tips数据集
## tips=pd.read_csv(r'D:/data/pydata-book-2nd-edition/examples/tips.csv')
## 两个函数效果基本相同,regplot:只能一对变量关系，适合多种格式的xy传递。lmplot()可以多对变量分析。
# sns.regplot(data=tips,x='total_bill',y='tip')
# plt.show()
## lmplot 小写的 l
# sns.lmplot(data=tips,x='total_bill',y='tip')
# plt.show()

## 离散值变量的回归
# sns.regplot(data=tips,x='size',y='tip')
# plt.show()

## 向离散值添加一些随机抖动，使分布更加清晰。抖动仅应用于散点图数据，不影响拟合.在x轴上分组，x_jitter=0.2 。偏移量加大为 0.2，使数据在x轴更加集中。
# sns.regplot(data=tips,x_jitter=0.2,x='size',y='tip')
# plt.show()

## 折叠每一个值，绘制均值的估计值和置信区间
# sns.regplot(data=tips,x='size',y='tip',x_estimator=np.mean)
# plt.show()

### 多变量之间的分析------lmplot()
## 探索三个变量关系
# sns.lmplot(data=tips,x='total_bill',y='tip',hue='smoker')
# plt.show()

## 在行列上进行分类,在三个变量影响下某两个变量的简单线性回顾关系
# sns.lmplot(data=tips,x='total_bill',y='tip',hue='smoker',row='time',col='sex')
# plt.show()
#print(tips.head())
# https://blog.csdn.net/qq_39949963/article/details/80773588
# https://cloud.tencent.com/developer/article/1517210

## 残差图检验回归模型---resiplot:在x轴上回归y,然后绘制残差的散点图
# sns.residplot(x='total_bill',y='tip',data=tips)
## 该结果出现异方差，效果不理想，seaborn无法实现。
# plt.show()

### 双变量多项式回归---这里是单因子多项式回归即一元多项式回归，指回归函数不能用直线来描述时。多项式回归属于非线性回归一种。参数 order:多项式次数。
anscombe=pd.read_csv('D:/data/seaborn-data-master/anscombe.csv')
##print(anscombe.head())
### 一次幂时，散点图呈抛物线形，
# sns.regplot(x='x',y='y',data=anscombe.loc[anscombe.dataset=="II"],scatter_kws={"s":80},order=1,ci=None)
# plt.show()
#### 改为2次幂，使其符合数据规律
# sns.regplot(x='x',y='y',data=anscombe.loc[anscombe.dataset=="II"],scatter_kws={"s":80},order=2,ci=None)
# plt.show()

#### 双变量分布---二维高斯分布----jointplot:展示两个变量关系与边缘分布。
### 二维高斯分布，以多元正太分布为例
## np.random.multivariate_normal:根据实际情况生成一个多元正态分布矩阵
# x,y=np.random.multivariate_normal([0,0],[(1,0),(0,1)],1000).T
# sns.jointplot(x,y)
# plt.show()
## 散点过多，用六边形代替散点
x,y=np.random.multivariate_normal([0,0],[(1,0),(0,1)],1000).T
sns.jointplot(x,y,kind='hex')
plt.show()

#### 皮尔森系数：两个变量之间相关系数越高，从一个变量去预测另一个的精度就高，皮尔森系数只对线性关系敏感。系数范围：0.2-1.0 越接近0.2，弱相关，近1.0，则是正相关。  导入 import scipy.stats as sci
sns.jointplot(x='total_bill', y='tip', data=tips, kind='reg', stat_func=sci.pearsonr)
## 相关性0.68 来自不相关性为6.7e-34（指：不相关系数小，结果可靠）
plt.show()





