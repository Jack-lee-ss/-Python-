### 绘制3月分和10月分的散点图
import matplotlib.pyplot as plt
import numpy as np
import random
import seaborn
import matplotlib

import pandas as pd
import seaborn as sns
from  matplotlib import font_manager
#from pandas.tests.io.excel.test_xlrd import xlrd

my_font=font_manager.FontProperties(fname="C:/Windows/fonts/msyhbd.ttc")
## 指定默认字体
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus']=False
## 解决负号’-‘显示为方块的问题
##  matplotlib.rcParams[‘axes.unicode_minus’] = False
# y_3=[11,17,16,11,12,11,12,6,6,7,8,9,12,15,14,17,7,8,9,14,15,15,15,19,21,22,22,23,17,32,12]
# # y_10=[7,8,9,15,14,17,7,12,6,6,11,17,16,19,21,22,22,23,17,11,12,11,12,12,15,14,6,23,12,26,14]
# # x_3=range(1,32)
# # x_10=range(41,72)
# # plt.scatter(x_3,y_3,label='3月份')
# # plt.scatter(x_10,y_10,label='10月份')
# # _x=list(x_3)+list(x_10)
# # xlabel_tick=['3月{}号'.format(i) for i in x_3]
# # xlabel_tick+=['10月{}号'.format(i-40) for i in x_10]
# # plt.xticks(_x[::3],xlabel_tick[::3],fontproperties=my_font,rotation=45)
# # # infos={
# # # 	'title':'温度散点图',
# # # 	'xlabel':'时间',
# # # 	'ylabel':'温度'
# # # }
# # plt.legend(loc='best',prop=my_font)
# # plt.title('温度散点图',fontproperties=my_font)
# # plt.xlabel('时间',fontproperties=my_font)
# # plt.ylabel('温度',fontproperties=my_font)
# # plt.savefig('./my third plot.png')
# # plt.show()

## 条形图绘制I
# a=['战狼2','哪吒之魔童降世','流浪地球','复仇者联盟4：终局之战','红海行动','美人鱼','唐人街探案2','我和我的祖国','我不是药神','中国机长','速度与激情8','西虹市首富','速度与激情7','捉妖记','复仇者联盟3:无限战争']
# b=[56.39,49.3,46.8,42.1,36.3,32.4,31.4,30.6,29.6,28.4,26.5,23.8,20.4,18.4,17.3]
# plt.figure(figsize=(20,8),dpi=80)
# plt.barh(a,b,height=0.5,color='r')
# plt.yticks(a,fontproperties=my_font)
# plt.grid(alpha=0.3)
# plt.savefig('./my fourth plot')
# plt.show()

# 条形图绘制II（竖向绘制）：电影在不同时间日(10,12,16,17)观影人数
# a=['战狼2','我和我的祖国','复仇者联盟3:无限战争','速度与激情7','我不是药神']
# b_10=[1234,3467,5678,2345,1234]
# b_12=[2345,3214,2341,7832,2345]
# b_16=[3456,6535,1234,2314,3456]
# b_17=[5232,2312,3435,6421,2345]
# bar_width=0.2
# x_10=list(range(len(a)))
# x_12=[i+bar_width for i in x_10]
# x_16=[i+bar_width*2 for i in x_10]
# x_17=[i+bar_width*3 for i in x_10]
#
# plt.bar(x_10,b_10,width=bar_width,label='9月10号')
# plt.bar(x_12,b_12,width=bar_width,label='9月12号')
# plt.bar(x_16,b_16,width=bar_width,label='9月16号')
# plt.bar(x_17,b_17,width=bar_width,label='9月17号')
#
# plt.xticks(x_12,a,fontproperties=my_font)
# plt.legend(loc='best',prop=my_font)
# plt.ylabel('单位：个',fontproperties=my_font)
# plt.title('九月电影观看人数',fontproperties=my_font)
# plt.savefig('./my fifth plot')
# plt.show()

## 横向绘制
# a=['战狼2','我和我的祖国','复仇者联盟3:无限战争','速度与激情7','我不是药神']
# b_10=[1234,3467,5678,2345,1234]
# b_12=[2345,3214,2341,7832,2345]
# b_16=[3456,6535,1234,2314,3456]
# b_17=[5232,2312,3435,6421,2345]
# plt.figure(figsize=(16,8),dpi=80)
# bar_height=0.2
# x_10=list(range(len(a)))
# x_12=[i+bar_height for i in x_10]
# x_16=[i+bar_height*2 for i in x_10]
# x_17=[i+bar_height*3 for i in x_10]
# plt.barh(x_10,b_10,height=bar_height,label='9月10号')
# plt.barh(x_12,b_12,height=bar_height,label='9月12号')
# plt.barh(x_16,b_16,height=bar_height,label='9月16号')
# plt.barh(x_17,b_17,height=bar_height,label='9月17号')
# plt.yticks(x_12,a,fontproperties=my_font)
# plt.legend(loc='best',prop=my_font)
# plt.xlabel('单位：个',fontproperties=my_font)
# plt.title('九月电影观看人数',fontproperties=my_font)
# ## bbox_inches='tight'：去掉周围空白部分
# plt.savefig('./my sixth plot',dpi=400,bbox_inches='tight')
# plt.show()

## Series 和 DataFrame 绘制图形，默认是折线图
# Series 和 DataFrame 对象的索引传入默认作为X轴，可以传入use_index=False禁用该功能
# s=pd.Series(np.random.randn(10).cumsum(0),index=np.arange(0,100,10))
# s.plot()
# plt.show()


# df=pd.DataFrame(np.random.randn(10,4).cumsum(0),columns=['A','B','C','D'],index=np.arange(0,100,10))
# df.plot()
# plt.show()

## 柱状图 注意 rand(),randn()区别：https://blog.csdn.net/m0_38061927/article/details/75335069

# fi,axes=plt.subplots(1,2)
# data=pd.Series(np.random.rand(8),index=list('abcdefgh'))
# data.plot.bar(ax=axes[0],color='k',alpha=0.4)
# data.plot.barh(ax=axes[1],color='b',alpha=0.4)
# plt.savefig('./my seventh1 plot')
# plt.show()
#
#
# fig,axes=plt.subplots(2,1)
# data=pd.Series(np.random.rand(8),index=list('abcdefgh'))
# data.plot.bar(ax=axes[0],color='k',alpha=0.4)
# data.plot.barh(ax=axes[1],color='r',alpha=0.4)
# plt.savefig('./my seventh2 plot')
# plt.show()
#
# # DataFrame中，柱形图将每一行的值分组并合并在一组中。
# # 竖直柱状图
# df=pd.DataFrame(np.random.rand(6,4),index=['one','two','three','four','five','six'],columns=pd.Index(['A','B','C','D'],name='Bob'))
# df.plot.bar()
# plt.savefig('./my eighth1 plot')
# plt.show()

## 横向柱状图和堆积柱状图
# a=['第一天','第二天','第三天','第四天','第五天','第六天']
# b=['one','two','three','four','five','six']
# df=pd.DataFrame(np.random.rand(6,4),index=a,columns=pd.Index(['A','B','C','D'],name='Bob'))
# # 堆积图 传入：stacked=True
# df.plot.barh(stacked=True,alpha=0.5)
# # plt.style.use('seaborn')
# # plt.savefig('./my eighth2 plot')
# plt.show()
# # 横向柱状图
# df.plot.barh(alpha=0.5)
# # plt.style.use('seaborn')
# # plt.savefig('./my eighth3 plot')
# plt.show()

## seaborn 库绘制图形
# tips=pd.read_csv(r'D:/data/pydata-book-2nd-edition/examples/tips.csv')
# # 交叉表
# party_counts=pd.crosstab(tips['day'],tips['size'])
# print(party_counts)
# print('----'*10)
# # 没有太多的1人和6人派对,切片
# party_counts=party_counts.loc[:,2:5]
# # div函数：将数据标准化，确保每一行的值和是1，然后绘图。
# party_pcts=party_counts.div(party_counts.sum(1),axis=0)
# print(party_pcts)
# party_pcts.plot.bar()
# #plt.show()
# print('----'*10)
#
# tips['tip_pct']=tips['tip']/(tips['total_bill']-tips['tip'])
# # tips.head()：打印前五行
# print(tips.head())
#
# sns.barplot(x='tip_pct',y='day',hue='time',data=tips,orient='h')
# sns.set(style='whitegrid')
# plt.show()

# tips=pd.read_csv(r'D:/data/pydata-book-2nd-edition/examples/tips.csv')
# #print(tips.head())
# sns.barplot(x='num',y='tip',color='blue',palette='husl',orient='v')
# plt.ylabel('GDP')
# plt.legend(loc='best')
# plt.show()

# tips['tip_pct'].plot.hist(bins=50)
# plt.show()
# tips['tip_pct'].plot.density()
# plt.show()
#
# comp1=np.random.normal(0,1,size=200)
# comp2=np.random.normal(10,2,size=200)
# values=pd.Series(np.concatenate([comp1,comp2]))
# sns.distplot(values,bins=100,color='k')
# plt.title('正太混合的标准化直方图与密度估计',fontproperties=my_font)
# plt.show()

## 散点图
a=pd.read_csv('D:/data/pydata-book-2nd-edition/examples/macrodata.csv')
#print(a.head())
data=a[['cpi','m1','tbilrate','unemp']]
b=np.log(data).diff().dropna()
print(b.head())
sns.regplot('m1','unemp',data=b)
plt.title('Change in log %s versus log %s' %('m1','unemp'))
plt.show()

sns.pairplot(b,diag_kind='kde',plot_kws={'alpha':0.2})
plt.show()



