# -*- coding: utf-8 -*-
class Cat:
	def __init__(self,new_name):   ## TOM 初始化形参 new_name.并赋值给 Tom 属性
		self.name=new_name
		print('%s 来了'% self.name)
	
	#def __del__(self):             # 调用 该方法，对象结束（该方法一般是最后调用的方法）
		print('俺走了')

	def __str__(self):
		return '我是小猫[%s]'%self.name # 该方法必须返回一个字符串，可以自定义返回值

Tom=Cat('TOM')                     # Tom 全局变量
print(Tom)                         # 无 __str__(self)时，打印输出 Tom 地址
print(Tom.name)					   # 打印 Tom 属性
print('=============')
#del Tom                       ## del 删除对象，一旦删除，则立即调用  __del__(self)
print('+++++++++')        ## 此时，++++ 最后打印出来，如果不删除对象，最后执行 __del__(self)
print(Tom,'\n')                ## 打印__str__(self) 名称属性

### 案例1--------------封装,多个对象互不影响，可以调用相同方法
class Person:
	def __init__(self,name,weight):
		self.name=name
		self.weight=weight
		
	def __str__(self):
		return "我的名字叫 %s 体重是 %.2f 公斤"%(self.name,self.weight)
	
	def run(self):
		print('%s 爱跑步，跑步锻炼身体'% self.name)
		self.weight-=1
		
	def eat(self):
		print('%s 是吃货'%self.name)
		self.weight+=1

XiaoMing=Person('小明',70)
print(XiaoMing)
XiaoMing.run()
XiaoMing.eat()
print('----------------------')
XiaoMei=Person('小美',45)
print(XiaoMei)
XiaoMei.eat()
XiaoMei.run()
print('--------------')
XiaoMing.run()
print('=================================')

######## 案例2---------家具安放，一般先开发被调用项，在开发调用项目

class HouseItem:
	def __init__(self,name,area):
		self.name=name
		self.area=area
		
	def	__str__(self):
		return '[%s] 占地 %.2f'%(self.name,self.area)
	

class House:
	def __init__(self,house_type,area):  # 初始化
		self.house_type=house_type
		self.area=area
		
		self.free_area=area # 剩余面积
		self.item_list=[]   # 添加家具的列表
	
	def __str__(self):
		# python 可以将括号内部代码连接一起
		return ('户型：%s\n总面积：%.2f[剩余面积]：%.2f\n家具：%s'
			   %(self.house_type,self.area,self.free_area,self.item_list))
	
	def add_items(self,item):
		print('要添加%s: '%item)
		# 判断家具面积
		if item.area> self.free_area:
			print('%s 的面积太大，无法添加'% item.name)
			return                                      # 无返回值代表结束 break
		self.item_list.append(item.name) # 添加家具到列表中
		self.free_area-=item.area # 计算剩余面积
		
## 创建家具
bed=HouseItem('席梦思',40)
chest=HouseItem('衣柜',8)
table=HouseItem('桌子',6)

print(bed)
print(chest)
print(table)

## 创建房子
my_house=House('两室一厅',50)
print(my_house)

my_house.add_items(bed)
my_house.add_items(chest)
my_house.add_items(table)
print(my_house)
print('=======================')

##### 封装案例3------------------一个对象属性可以是另一个类创建的对象
class Gun:
	def __init__(self,mode):
		self.mode= mode # 枪的类型
		self.bullet_count=0 # 子弹的数量
	
	def add__bullet(self,count):  # 添加子弹
		self.bullet_count+=count
		
	def shoot(self):
		if self.bullet_count<= 0:  # 判断是否有子弹
			print('%s 没有子弹'%self.mode)
			return
		self.bullet_count-=1       # 发射子弹，减少数量
		print('[%s]突突突。。。剩下[%d]颗子弹'%(self.mode,self.bullet_count))
		

class Soilder:
	def __init__(self,name):
		self.name=name
		#  新兵没有枪
		self.gun=None    # 属性为空对象
	
	def fire(self):
		if self.gun is None:    # 判断是否有枪
			print('[%s]还没有枪'%self.name)
			return
		print('冲鸭。。。。[%s]'%self.name)
		
		self.gun.add__bullet(78)           # 装子弹，枪对象调用装子弹方法
		self.gun.shoot()                   # 开枪    枪对象调用开枪方法
		
gun=Gun('AK47')
XuSanDuo=Soilder('许三多')
XuSanDuo.gun=gun             # 将枪对象赋给士兵属性，一个对象属性可以是另一个类创建的对象

XuSanDuo.fire()
print('================')

### 注意：身份运算符：比较两个对象的内存地址是否一致，针对 None 比较时，建议 is。is 用于判断两个变量对象是否同一个；==判断变量值是否相等。

####  私有属性和私有方法
## 私有属性
class Women:
	def __init__(self,name):
		self.name=name
		self.age=18
		self.__habit='睡觉'
	
	def secret(self):
		print('%s 的年龄是 %d,爱好是%s'%(self.name,self.age,self.__habit))

XiaoFang=Women('小芳')
print(XiaoFang.age)
XiaoFang.secret()       ##   调用方法可以获得
#print(XiaoFang.__habit) ## __habit:外部无法调用属性，由于加上了两个__ 属于私有属性，只能内部调用
print(XiaoFang._Women__habit)  ## _类名__属性：可以调用内部属性数据

print('------------------------------------')

## 私有方法

class Women:
	def __init__(self, name):
		self.name = name
		self.age = 18
		self.habit = '睡觉'
	
	def __secret(self):
		print('%s 的年龄是 %d,爱好是%s' % (self.name, self.age, self.habit))

XiaoFang = Women('小芳')
print(XiaoFang.age)
print(XiaoFang.habit)
#XiaoFang.__secret()    ## 外部无法调用添加两个__的方法。

XiaoFang._Women__secret()  ## _类名_方法：可以调用内部方法数据


