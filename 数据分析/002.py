## 折线图/散点图plot /直方图hist
import matplotlib.pylab as pyl
import numpy as npy
x=[1,2,3,4,8]
y=[5,7,2,1,5]
pyl.plot(x,y,"*r--") # plot(x轴数据，y轴数据，展现形式颜色)
pyl.title("show")
pyl.xlabel("ages")
pyl.ylabel("temp")
pyl.xlim(0,20)
pyl.ylim(0,12)
pyl.show()
#pyl.plot(x,y,"ob") ## "o" : 代表散点图
#pyl.show()
## 设置图形颜色： c:青色 r:红色 m:品红 g:绿色 b:蓝色 y:黄色 k:黑色 w:白色 。颜色可以叠加
## 设置线条形式：—— 直线 ---虚线 -.-.线点式 :细小虚线
## 点的样式：s:方形 h:六角形 H：六角形 *：星形 +：加号 d:菱形 p:五角形

### 随机数的生成
import numpy as npy
i=npy.random.random_integers(1,20,100) ##(最小值，最大值，个数)
j=npy.random.randint(1,20,20)
print(i)
print(j)

### 正态分布随机数
import numpy as npy
a=npy.random.normal(10.0,6.0,10)## (均数，标准差，个数)
print(a)

### 直方图绘制 hist
b=npy.random.normal(10.0,7.0,100)
sty=npy.arange(1,17,4) ### 设置x轴间距，1到17 步长 为4
pyl.hist(b,sty)
#pyl.show()
c=npy.random.random_integers(1,25,100)
#pyl.hist(c, bins=10, edgecolor='black', linewidth=1) ## pyl.hist(c,histtpe='stepfilled'):取消图形间轮廓，
#pyl.show()

#### 绘制直方图子图 pyl.subplot()
import numpy as npy
a=npy.random.random_integers(1,200,100)
#sty=npy.arange(1,50,4)
pyl.subplot(2,2,1)### 行，列 ，当前区域 2行2列里绘制在第一行第1列
pyl.subplot(2,2,2)
pyl.subplot(2,1,2)

pyl.show()


###### 读取数据并且可视化  注意需要安装 xlrd 文件，才可以导入Excel;用Excel转化为CSV文件时，需要另存为csv格式，不要用原件导入pycharm中
import pandas as pda
import numpy as  npy
import matplotlib.pylab as pyl
i=pda.read_csv("D:/data/shuju.csv")
j=i.shape # 查看数据行数和列数
x=i.values[1][1]  ## 去表头后 ，即从CSV文件的第二行开始，将第二行作为数组中的[0] values[1][1]:表示源文件去表头后第三行第二列
y=i.values ## 获取所有数据
z=i.T  ### 转置数据，行列互换
a=z.values  ## 获取所有转置后的数据
b=z.values[2] ## 获取所有转置后第三行的数据
print(b)
