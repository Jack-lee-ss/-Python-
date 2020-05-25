## ================== 绘图与可视化======================
import random

import matplotlib.pyplot as plt
import numpy as np
# data=np.arange(10)
# print(data)
# print(plt.plot(data))
# plt.show()
# # 设置图片宽高 plt.figure()
# fig=plt.figure(figsize=(20,8),dpi=50)
# # 添加子图 fig.add_subplot() 2x3 共6个图，序号从1开始
# a=fig.add_subplot(2,3,1)
# b=fig.add_subplot(2,3,2)
# c=fig.add_subplot(2,3,4)
# # 只在最后一个子图上绘制图片
# # plt.plot([1.2,5,8,-4,2,0,12])
# # 绘图
# plt.plot('r--')
# # 保存图片
# plt.savefig('./picture1.png')
# plt.show()
# print('------'*10)


# plt.figure(figsize=(20,8),dpi=50)
# # x y 数据个数要相同
# x=range(2,12,2)
# y=[1.2,5,8,-4,2]
# # 制图
# plt.plot(x,y,'g--')
# # 保存图片
# plt.savefig('./picture.png')
# # 展示图片
# plt.show()
# print('------'*10)


## 刻度，标签，颜色，标记和线类型
# plt.figure(figsize=(20,8),dpi=50)
# x=range(2,12,2)
# y=[1.2,5,8,-4,2]
# # xlim:限定x轴范围（即x轴最大边界值）
# plt.xlim([0,14])
# # xticks:刻度大小
# plt.xticks(range(2,12,5))
# # 给x轴设置标签
# plt.xlabel("num")
# plt.plot(x,y,'b--')
# plt.show()
from matplotlib import font_manager

# print('---'*10)
#
# ## 绘制9点到12点3小时内气温折线图---------------ctrl+B：查看原函数用法
# plt.figure(figsize=(20,8),dpi=60)
# x=range(0,180)
# # x轴上从0到180分钟内任意时间对应一个温度值
# y=[random.randint(20,40) for i in range(180)]
# plt.xticks(range(0,180,15))
# plt.yticks(range(20,41,1))
#
# # 调整x轴刻度及中文注释
# a=['9点{}分'.format(i) for i in range(60)]
# a+=['10点{}分'.format(i) for i in range(60)]
# a+=['11点{}分'.format(i) for i in range(60)]
#
# # 设置中文字体 在cmd找那个输入：fc-list :lang=zh 注意冒号前有空格，查找中文字体，如：C:/Windows/fonts/STSONG.TTF。导入 font_manager 字体管理库。
# my_font=font_manager.FontProperties(fname="C:/Windows/fonts/msyhbd.ttc")
#
# # 转为列表切片下，取步长与数字和字符串一一对应,rotation=45 旋转45°
# plt.xticks(list(x)[::5],a[::5],rotation=45,fontproperties=my_font)
#
# # 添加描述信息
# plt.xlabel('时间',fontproperties=my_font)
# plt.ylabel('温度 单位℃',fontproperties=my_font)
#
# # 添加网格以及设置透明度
# plt.grid(alpha=0.5)
#
# # 绘制
# plt.plot(x,y,'r')
# plt.savefig('./温度变化图.png')
# plt.show()
# print('----'*10)

## 双线条绘制
# plt.figure(figsize=(20,8),dpi=60)
# y_1=[10,12,25,8,-4,22,16,3]
# y_2=[7,23,14,27,12,4,6,12]
# x=range(2,10)
#
# # 定义线条名
# plt.plot(x,y_1,label="自己" 'r' '-.')
# plt.plot(x,y_2,label="他人" 'c' ':')
#
# # 设置字体
# my_font=font_manager.FontProperties(fname="C:/Windows/fonts/msyhbd.ttc")
#
# # 刻度大小
# xlable=["{}岁".format(i) for i in x]
# plt.xticks(x,xlable,fontproperties=my_font)
#
# # 添加描述信息
# plt.xlabel('年龄',fontproperties=my_font)
# plt.ylabel('次数 单位 个',fontproperties=my_font)
#
# # 添加网格以及设置透明度
# plt.grid(alpha=0.5)
#
# # 添加图例
# plt.legend(prop=my_font,loc='upper left')
#
# # 保存图片
# # plt.savefig('./不同年龄个数图.png')
# plt.show()
# print('----'*10)

'''
y_1=[10,12,25,8,-4,22,16,3]
y_2=[7,23,14,27,12,4,6,12]
x=range(2,10)
fig=plt.figure()
ax=fig.add_subplot(1,1,1)
my_font=font_manager.FontProperties(fname="C:/Windows/fonts/msyhbd.ttc")
ax.plot(x,y_1,'c--',label='自己',fontproperties=my_font)
ax.plot(x,y_2,'r',label='他人',fontproperties=my_font)
# 输入汉字
ax_xlable=["{}岁.format(i) for i in x"]
ticks=ax.set_xticks(x,ax_xlable)
plt.legend(loc='best')
infos={
	'title':'My second plot',
	'xlabel':'年龄',
	'ylabel':'个数'

}
ax.set(**infos)
# ax.set_title('My first plot')
# ax.set_xlabel('stages')
#ax.set_ylable('num')
plt.grid(alpha=0.5)
plt.show()

'''

### 多子图的创建与绘制
'''
fig=plt.figure()
ax1=fig.add_subplot(2,2,1)
ax2=fig.add_subplot(2,2,2)
ax3=fig.add_subplot(2,2,3)
plt.plot(np.random.randn(50).cumsum(),'k--')
b=ax1.hist(np.random.randn(100),bins=20,color='k',alpha=0.3)
ax2.scatter(np.arange(30),np.arange(30)+3*np.random.randn(30))
fig,axes=plt.subplot(2,2,3)
print(axes)
'''
### 随机漫步折线图
# fig=plt.figure()
# ax=fig.add_subplot(1,1,1)
# ax.plot(np.random.randn(1000).cumsum(),'k--',label='two')
# ax.plot(np.random.randn(1000).cumsum(),'k',label='one')
# ax.plot(np.random.randn(1000).cumsum(),'k.',label='three')
# ticks=ax.set_xticks([0,200,400,600,800,1000])
# labels=ax.set_xticklabels(['one','two','three','four','five','six'])
# ax.set_title('My first plot')
# ax.set_xlabel('stages')
# ax.legend(loc='best')
# plt.savefig('./My first plot.png')
# plt.show()

### 绘制散点图


