## ================== numpy 数组===================
# 创建数组 array函数
import numpy as np
a=[2,4,8.9,3]
b=np.array(a) ## 生成数组
print(b) # 由于出现小数，所以数组化为0.1形式

c=np.random.randn(3,3) # 生成随机数，3行3列
print(c)
print(c.shape) # 3个维度，一个维度3个数值
print(c.dtype) # 数组dtype属性 数据类型

## range 函数
d=np.arange(12) ## 内建函数 range 的数组版
print(d)

## 全1数组
e=np.ones((2,4)) ## 2维4数值
print(e)

### 数组数据类型 astype 方法
# 浮点数转化成整数
a=np.array([3.4,5.6,7.3,3,3,-7.4,-0.3]) #浮点型数据
print(a)
b=a.astype(np.int32) #浮点变成整数，整数变小，负数变大，去小数
print(b)
a=np.array([2,4,6,7])
b=a.astype(np.float64) # 整数化为浮点数，后有一位小数点
print(b)

## 字符串变数字
a=np.array(['1.23','4.5','-4.3'])
b=a.astype(float) ## 含小数的需用 float
print(b)

### numpy 数组算术
# 数组的标量计算
a=np.array([[1,2,3],[4,5,6]])
print(a)
b=a*a ## 对应项数学运算 注意：同尺度
print(b)

# 同尺度数组间比较 返回布尔值
c=a>b
print(c)

### 索引与切片
# 数组取值与赋值
a=np.arange(10) # 自动生成
print(a)
b=a[4:7] ## 类似 列表切片
print(b)
print(a[4:7].copy()) ## 效果同上，切片的拷贝数据
a[5:7]=44 ## 赋值
print(a)
b[1]=100 ##改变切片中某一个数值，整个数组发生变化
print(a)
b[:]=99 ## 切片将被引用到所有值上
print(a)

### 二维数组中，每一个索引值对应一个一维数组，而不是元素，索引代表数组维度
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a[2])
print(a[1][2]) # 单个元素要两层索引值。

### 多维数组
a=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(a)
print(a[0]) ## 外围第一层 ，数组第0层 返回二维数组
print(a[1][0])## 外围第二层，中围第一层。返回一维数组
print(a[1][0][1])## 外围第二层，中围第一层，内围第二层 返回值

## 多维数组的切片 --- 一层一层索引，从大范围到小范围
# 二维数组切片
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a[:2]) # 大范围，前两行，2-0=2,返回二维数组
print(a[:2][1]) # 返回的是二维数组的第二位数组，结果为一维数组
print(a[2,1]) #取某一个值，等价 a[2][1]

## 三维数组
a=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(a[0]) ## 返回二维数组
print(a[1,0]) ##返回一维数组
print(a[1,0,2]) # 返值
print(a[:,:1]) # 单独：选择整个轴上的数组，:1 表示第一层数组
print(a[:,:1,1]) #获得上层数组的第二个值
a[:,:1,1]=0 ## 给切片赋值，改变整个数组内容
print(a)

## 二维数组之神奇索引
a=np.empty((8,4))
for i in range(8):
	a[i]=i
print(a)
b=a[[2,3,5]] ## 用整数索引数据
print(b)
b=a[[-1,-5]] ## 从尾部开始的负索引
print(b)

a=np.arange(32).reshape((2,2,8)) ## 获取高维数组方法，32=2*2*8
print(a)

a=np.arange(32).reshape((8,4))
print(a)
b=a[[1,5,7,2],[0,3,1,2]]## 第一列数组为原数组第一项，第二列为第几个
print(b) # 即（1,0),(5,3)......被选中，对应关系

### 数组转置和换轴
a=np.arange(10).reshape((2,5))
print(a)
b=a.T ## 横纵互换
print(b)

a=np.arange(12).reshape((2,2,3))
print(a)
print(a.T)
print(a.transpose(2,1,0)) ## 等价于 （a.T）
print(a.transpose(0,2,1))
print(a.transpose(1,2,0))
print(a.transpose(2,0,1))

## 条件逻辑的数组操作 np.where
a=np.random.randn(4,4)
print(a)
print(a>0) ## 判断大小，返回布尔值
b=np.where(a>0,3,-3) ## 条件判断，类似If条件句 赋值3
print(b)
print(np.where(a>0,7,a)) # 大于0赋值为7 否则保原数组

### 布尔值数组法
a=np.random.randn(10)
print((a>4).sum()) ## 输出随机值大于4的值的计数

bools=np.array([False,True,True,False])
print(bools.any()) ## any：是否至少存在一个true
print(bools.all()) ## all：是否每个值都是true


