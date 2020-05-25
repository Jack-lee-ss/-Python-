# -*- coding: utf-8 -*-
## 继承的概念：子类拥有父类的所有方法和属性 class 类名（父类名）
# class Animal:
# 	def eat(self):
# 		print('eat')
#
# 	def drink(self):
# 		print('drink')
#
# 	def run(self):
# 		print('run')
#
# class Dog(Animal):    # 子类拥有父类的所有方法和属性 class 类名（父类名）
#
# 	def sleep(self):
# 		print('sleep')
#
# 	def bark(self):
# 		print('bark')
#
# WangCai=Dog()
# print(WangCai)
# WangCai.run()      ## 子类继承父类方法 ，下同
# WangCai.eat()
# WangCai.sleep()
# WangCai.bark()
# WangCai.drink()
# print('=========================')

## 继承传递性
# class Animal:
# 	def eat(self):
# 		print('eat')
#
# 	def drink(self):
# 		print('drink')
#
# 	def run(self):
# 		print('run')
#
# class Dog(Animal):
# 	def sleep(self):
# 		print('睡觉')
#
# class XiaoTianQuan(Dog):
# 	def bark(self):
# 		print('旺旺叫')
#
# xtq=XiaoTianQuan()
# xtq.bark()      # 调用本身的方法
# xtq.sleep()     # 调用父类方法
# xtq.eat()       # 调用父类的父类方法-------继承所有上层的方法，只有有继承关系才能调用

##########  方法的重写------ 子类对父类方法的修改，在调用子类同名方法时，只会调用子类方法
# class Animal:
# 	def eat(self):
# 		print('eat')
#
# 	def drink(self):
# 		print('drink')
#
# 	def run(self):
# 		print('run')
#
# class Dog(Animal):
# 	def sleep(self):
# 		print('睡觉')
#
#
# class XiaoTianQuan(Dog):
# 	def bark(self):
# 		print('旺旺叫')
#
# 	def run(self):
# 		print('跑得快')
#
# 	def sleep(self):
# 		print('睡得香')  # 输出子类方法内容
#
# 		## 两种调用父类方法：
# 		super().sleep()	 # 调用父类方法   super().父类方法
# 		super().run()
#
# 		Dog.sleep(self)  # 调用父类方法   父类名.父类方法
#
# 		print('睡一天')  # super 后，添加其他代码
#
# xtq=XiaoTianQuan()
# xtq.sleep()               # 在调用子类同名方法时，只会调用子类方法
# xtq.run()				  # # 在调用子类同名方法时，只会调用子类方法


##### 私有属性和方法的获取
# class A:
# 	def __init__(self):
# 		self.num1=100     # 共有属性，子类，内外均可调用
# 		self.__num2=200   # 私有属性，子类，外部不可调用
#
# 	def __test(self):     # 私有方法，子类，外部不可调用
# 		print('私有方法 %d %d'%(self.num1,self.__num2))
#
# 	def test(self):       # 共有方法，子类，内外可调用
# 		print('公有方法 %s'% self.__num2)
#
# 	def test1(self):
# 		print('间接访问私有方法 %s'%self.__test())
#
# class B(A):
# 	def demo(self):
# 		# 子类对象中，不能访问父类私有属性
# 		# print('访问父类私有属性 %d'% self.__num2)
# 		# 子类不能调用父类私有方法
# 		# self.__test()
# 		self.test()     # 子类调用父类共有方法间接访问父类私有属性或者方法
# 		self.test1()
# b=B()
# print(b.demo())
#
# ####  多继承------ 子类可以继承多个父类的属性和方法
# class A:
# 	def test1(self):
# 		print('abd')
#
# class B:
# 	def test2(self):
# 		print('bgn')
#
# class C(A,B):  ###  继承多个父类方法或者属性 ，避免父类方法或者属性同名，不然调用出问题
# 	pass
# c=C()
# c.test1()
# c.test2()

###### MRO：方法搜索顺序  __mro__:多继承调用顺序

# class A:
# 	def test(self):
# 		print('A---abd')
# 	def demo(self):
# 		print('A---abc')
#
# class B:
# 	def test(self):
# 		print('B--bgn')
# 	def demo(self):
# 		print('B--abc')
#
# class C(A, B):  ###  继承多个父类方法或者属性,__mro__调用搜索顺序
# 	pass
# c = C()
# print(C.__mro__) ## 类名.__mro__:搜索顺序，从左往右，依次查找
# c.test()
# c.demo()
#
# ###  新式类
# class D:   ## python 3. 不加父类名，默认为class D(object),属性多
# 	pass
# d=D()
# print(dir(d)) # 查看属性

######## super().__init__()用法 ：继承父类的子类调用父类的初始化方法，参数可以不同
# class Person():
#     def __init__(self,name,age):  ## 初始化属性
#         self.name=name
#         self.age=age
#
#     def name1(self,name):          #定义方法名时不要和变量名一样，否则在调用的时候可能会报错。
#         print('方法中名字 %s'%name) # 传递
#         print('类中的名字 %s'%self.name)
#
#     def age1(self,age):
#         print('方法中的年龄 %s' %age)
#         print('类中的年龄 %s' %self.age)
#
#
# class New_person(Person):
#     def __init__(self,new_name,new_age,sex):  ### 初始化 New_person
#         super().__init__(new_name,new_age)    ##  调用父类初始化方法
#         self.sex=sex                          #   自定义子类专有属性
#
#     def diaoyong(self,name,age):
#         self.name1(name)
#         self.age1(age)
#         print('类中的性别 %s' % self.age) ## 继承父类的参数，同上
#
#     def sex1(self,sex):
#         print('方法中的性别 %s' %sex)       ## 传递给方法中的参数
#         print('类中的性别 %s' %self.age)
#         print('类中的性别 %s' %self.sex)    ## 子类中新定义的参数
#
# # 由于super().__init__(new_name,new_age)：继承了父类初始化属性，子类New_person('小花','20','男') 传递的数据也就是父类 Person() __init__(self,name,age)中的数据
# new_p=New_person('小花','20','男')
#
# # 调用new_p.diaoyong('小米','15')，将数据通过子类 diaoyong 方法，寻找父类方法self.name1，self.age1。打印出各自数值，%name：父类方法中的数据，也就是传入数据，%self.name：父类初始化数据。
# new_p.diaoyong('小米','15')
#
# # 同上
# new_p.sex1('女')

####  super()本质：多继承里，指调用者节点位置的广度优先顺序，而不是直接找父类
class A(object):
	def func(self):
		print('A')

class B(A):
	def func(self):
		super().func()
		print('B')
	
class C(A):
	def func(self):
		super().func()
		print('C')

class D(B,C):
	def func(self):
		super().func()
		print('D')
d=D()
d.func()
print(D.__mro__)
