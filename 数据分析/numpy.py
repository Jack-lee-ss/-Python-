# 生活不会突变，你要做的只是耐心和积累。人这一辈子没法做太多的事情，所以每一件尽力而为。
# -*- coding: utf-8 -*-

### python 原生语法实现：
'''
import time
t1=time.time()
def sum(n):
	a=[i**2 for i in range(n)]
	b=[i**3 for i in range(n)]
	c=[]
	for i in range(n):
		c.append(a[i]+b[i])
	return c
sum(1000*100)
print('Python运行耗时:%f'%(time.time()-t1)) # 0.190879
print()

## numpy() 实现：
import numpy as np
t2=time.time()
def sum(n):
	a=np.arange(n)**2
	b=np.arange(n)**3
	return a+b
sum(1000*100)
print('numpy运行耗时:%f'%(time.time()-t2))  # 0.001999
'''
'''
  array()本身属性：
  	shape:返回一个元组，表示array的维度
  	ndim:一个数字，表示array的维度数目
  	size：一个数字，表示array中所有数据元素的数目
	dtype: array中元素的数据类型
 
'''
## 创建array数组
import numpy as np
s=np.array([1,2,3,4,5,6,7,8])   ## 一维数组
print(s)
print(s.shape)                   # (8,) 一维数组，共8元素
print(s.ndim)
print(s.size)
print(s.dtype)

l=np.array(
	[
		[1,2,3,4],
		[5,6,7,8]
	]
)
print(l)                        # 二维数组
print(l.shape)                  # (2, 4) 两行，四列
print(l.ndim)                   #  2   维度
print(l.size)                   #  8   元素个数
print(l.dtype)                  #  int32 类型


print(np.arange(10))

print(np.arange(1,10,2))

print(np.ones(10))           ## 自己设置数组，一维10个数字全是1的向量

print(np.ones((3,6)))         # 设置数组结构 二维3行6列全是1的向量

print(np.ones_like(s))       ## 传递一个已经存在的数组，但是数值全变成 1
print(np.ones_like(l))
print()

###   np.zeros和np.zeros_like 同上，全为 0

print(np.full(10,67))
print(np.full((3,4),88))

print(np.full_like(s,99))
print(np.full_like(l,78))

print(np.random.randn())        ## 一个随机数
print(np.random.randn(2))        # 两个随机数
print(np.random.randn(2,4))      # 2行4列二维随机数
print('===============')
print(np.random.randn(2,3,4),'\n')    # 3维数组


print(np.random.randn(10).reshape(2,5))  ## 随机10个数，2行5列
print(np.arange(10).reshape(2,5))         # 0-9共10个数，2行5列

## 数学计算
print(np.arange(8).reshape(2,4)*2+3)    ## 每一个数字 *2+3
print(np.sin(np.arange(8).reshape(2,4))) # 求sin()函数
print(np.exp(np.arange(8).reshape(2,4)*2+3)) # 求每一个数的 e 的 x 次方
print()

## 对应数组相加减：
print(np.random.randn(10).reshape(2,5)+np.random.randn(10).reshape(2,5))
print(np.random.randn(10).reshape(2,5)-np.random.randn(10).reshape(2,5))

print('+++++++++++++++++++')
## 二维数组的索引和切片
s=np.arange(20).reshape(4,5)

print(s[2])          ## 取第3行
print(s[-1])         #  最后一行
print(s[:-1])        #  除去最后一行

print(s[:2,3:])      #  取前2行的3,4列
print(s[:3,4])       #  前3行的第3列

print(s[[1,3]])      #   取多个不连续行
print(s[[0,2,3]])

print(s[:,[2,3]])    # 行不能省略，列取多个

print(s[[1,2,3],[0,1,2]]) # 返回一维数组


print('**************')

print(s[0,0])
print(s[0][0])
print(s[0,0]==s[0][0])

print(s[2,4])
print(s[-3,2])

## 切片的修改会修改原来的数组，原因：numpy会经常处理大数据，避免每次复制
## 布尔索引
s=np.arange(20)
s[s>13]=10
s[s<5]=1.2
print(s[s<9]+30)
s[s<9]+=30
print(s,'\n')


s=np.arange(20).reshape(4,5)
print(s>8)
print(s[s>8],'\n')
print(s[:,4])          ### 所有行的第4列

print(s[3])              # [15 16 17 18 19] 最后一行
print('')

print(s[:-1])            # 除去最后一行
print(s[s[:,4]>7])
s[s>13]=10
s[s<5]=1.2
print(s[s<9]+30)
s[s<9]+=30
print(s)

print('================ 随机数函数 =============')
## rand():返回数据在[0,1]之间
print('******** rand()函数 *********')

print(np.random.rand(5),'\n') ## 生成5个数据在[0,1]之间的数据

print(np.random.rand(2,3),'\n') # 2行3列 6个随机数

print(np.random.rand(2,3,4))
print('\n')

## randn():返回数据具有正太分布（均值0，方差1）
print('********** randn()函数 *******')
print(np.random.randn(4),'\n')

print(np.random.randn(3,4),'\n')

print(np.random.randn(2,3,4))
print()

## randint():生成随机整数，
print('********** randint() **********')

print(np.random.randint(3))            ## 0-2之间 随机整数

print(np.random.randint(1,5))           # 1-4之间，随整数

print(np.random.randint(10,30,size=(5,)))   # 10-30之间，一维5个随机数

print(np.random.randint(10,30,size=(2,4,5))) # 10-30之间，三维2*4*5=40个数
print()

print('========== random()函数 ==========')
### random():生成[0.0, 1.0] 随机数
print(np.random.random(4))

print(np.random.random(size=(3,4)))

print(np.random.random(size=(2,3,4)))
print()

print('======== choice ========')
## a是一维数组，从它里面生成随机结果
print(np.random.choice(7,4))  ## 从range(7)中随机生成4个数

print(np.random.choice(10,(2,3)))  # 从range(10)中生成（2,3）数组

print(np.random.choice(range(20),(3,4)))

print(np.random.choice([3,6,1,9],(2,2)))
print()


print('============= shuffle =============')
a=np.arange(10)
np.random.shuffle(a)
print(a)  ## 把数组数字进行随机排列,对元素组重排,permutation():不会改变原数组，产生新数组
print()

a=np.arange(10).reshape(2,5)
np.random.shuffle(a)
print(a)


print('=========== normal(均值，方差，个数)函数 ===========')
## 按照均值和方差生成高斯分布的数字,自己设定
print(np.random.normal(3,5,10))

print(np.random.normal(4,6,(3,4,2)))
print()

print('============ uniform(最小，最大，个数)函数 ========')
## 在指定大小之间生成均匀分布数字
print(np.random.uniform(1, 9, 4))

print(np.random.uniform(1, 9, (2,3)))
print()

'''
		## 实例，加入噪声
		import matplotlib.pyplot as plt
		x=np.linspace(-10,10,100)
		y=np.sin(x)+np.random.randn(len(x))   ## 给规整曲线加入噪声
		plt.plot(x,y)
		plt.show()

'''
print('============ numpy中数学统计函数 ======= ')
a=np.arange(12).reshape(3,4)
print(np.sum(a))   ## 未设定 axis 默认一维,求和
print(np.prod(a))   # 求积
print(np.cumsum(a)) # 计算累计和
print(np.cumprod(a))# 计算累积
print(np.min(a),np.max(a))

print(np.percentile(a,[0.23,0.54]))  ## 计算一个数组中的几分位数
print(np.median(a),np.mean(a))
print(np.std(a),np.var(a))   ## std:标准差； var:方差
print()

## axis=0 计算行值（竖着算）和 axis=1 计算列值（横着算）
a=np.arange(12).reshape(3,4)
print(np.sum(a,axis=1))
print(np.sum(a,axis=0))

print(a.sum(axis=0))
print(a.cumsum(axis=1))
print()


### 机器学习数据的标准化 A=(A-mean(A,axis=0))/std(A,axis=0))
##  均匀的数据使用：
a=np.arange(12).reshape(3,4)
mean=np.mean(a,axis=0)

std=np.std(a,axis=0)

fenzi=a-mean       ## 广播机制，数组中每一个值均减去均值

result=fenzi/std
print(result,'\n')

## 随机数使用：
a=np.random.randint(1,100,size=(3,4))
mean=np.mean(a,axis=0)

std=np.std(a,axis=0)

fenzi=a-mean       ## 广播机制，数组中每一个值均减去均值

result=fenzi/std
print(result)
print()

print('=========== 增维与降维 ========')
#### 增加维度
a=np.arange(10).reshape(2,5)
print(a)
print(a.shape)

# np.newaxis
print(np.newaxis is None)
print(np.newaxis==None)

print(a[np.newaxis,:])   ## 增加一个行维度
print(a[np.newaxis,:].shape)

print(a[:,np.newaxis])    # 增加一个列维度
print(a[:,np.newaxis].shape)
print()


## np.expand_dims()
print(np.expand_dims(a,axis=0))
print(np.expand_dims(a,axis=0).shape)
print(np.expand_dims(a,axis=1))
print(np.expand_dims(a,axis=1).shape)
print()

## np.reshape()
print(np.reshape(a,(1,-1)))
print(np.reshape(a,(-1,1)))
print(np.reshape(a,(1,-1)))
print(np.reshape(a,(-1,1)))