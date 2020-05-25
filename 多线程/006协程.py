# -*- coding: utf-8 -*-
### 迭代器
import time
from collections import Iterable, Iterator
class classmate(object):
	def __init__(self):
		self.names=list()
		self.current_num = 0
		
	def add(self, name):
		self.names.append(name)
		
	def __iter__(self):
		''' 要想使用 for 迭代，必须用 __iter__方法'''
		return self

	def __next__(self):
		if self.current_num<len(self.names):
			ret=self.names[self.current_num]
			self.current_num+=1
			return ret
		else:
			raise StopIteration
	
classmate=classmate()
classmate.add('老王')
classmate.add('张三')
classmate.add('李四')
# print('判断classmate是否是可以迭代的对象：', isinstance(classmate,Iterable)) # Ture；迭代对象；Flase:不是
# classmate_itrator=iter(classmate)
# print('判断classmate_itrator是否是迭代器：', isinstance(classmate_itrator,Iterator))
# print(next(classmate_itrator))
for name in classmate:
	print(name)
	time.sleep(1)
	
######  斐波那契数列
# class Fibonacci(object):
# 	def __init__(self,all_num):
# 		self.all_num=all_num
# 		self.current_num=0
# 		self.a=0
# 		self.b=1
#
# 	def __iter__(self):
# 		return self
#
# 	def __next__(self):
# 		if self.current_num < self.all_num:
# 			ret=self.a
# 			self.a, self.b=self.b, self.a+self.b
# 			self.current_num+=1
# 			return ret
# 		else:
# 			raise StopIteration
#
# fibo=Fibonacci(100)
#
# for num in fibo:
# 	print(num)
	
#########  生成器--------特殊的迭代器
def creat_num(all_num):
	#print('---1----')
	a, b=0, 1
	current_num= 0
	while current_num< all_num:
		#print('----2----')
		yield a                # 出现yield语句的函数，不再是函数，而是生成器模板
		#print('----3-----')
		a, b= b,a+b
		current_num+=1
		#print('----4-----')
	return 'ok----'

obj= creat_num(20)             # 调用函数中有yield，则不是调用函数，而是生成器对象
while True:
	try:
		ret=next(obj)		   # next():继续下一个数据，启动生成器
		print(ret)
	except Exception as ret:
		print(ret.value)       ## 打印返回值
		break
		

## 通过send 启动生成器
def creat_num(all_num):
	a, b=0, 1
	current_num= 0
	while current_num< all_num:
		ret= yield a          # 出现yield语句的函数，不再是函数，而是生成器模板，先停止，将 a 返回给 ret ，打印出来。
		print('>>ret>>:',ret)
		a, b= b,a+b
		current_num+=1
obj= creat_num(20)             # 调用函数中有yield，则不是调用函数，而是生成器对象
ret=next(obj)          # 将 a 赋给 ret ,打印出来，返回循环体，此时， ret = None
print(ret)
ret=next(obj)		   # 再次调用生成器，将 a=1 赋给 ret, 打印出来，但其后是 send,需要先传入数据
print(ret)
ret=obj.send('hahahhah')      # send 可以传值，但不打印send下面语句，传入后而是执行循环体内语句
print(ret)					  # 等再次执行 yield 时，将 yield 后面的值返回给 send ,传给 							  # ret,打印出来。send 一般首次不使用。
ret=obj.send('你好')
print(ret)


#### yield 多任务------并发类（假的并行，交替调用）
# def task_1():
# 	while True:
# 		print('-----1----')
# 		time.sleep(0.5)
# 		yield
#
# def task_2():
# 	while True:
# 		print('-----2----')
# 		time.sleep(0.5)
# 		yield              # 单独 yield 表示暂停
#
# def main():
# 	t1=task_1()
# 	t2=task_2()
# 	while True:
# 		next(t1)		   # 循环调用两个函数
# 		next(t2)
#
# if __name__ =='__main__':
# 	main()


#### gevent 多任务
import gevent
import time
from gevent import monkey

monkey.patch_all()  # 有耗时操作需要导入

def f1(n):
	for i in range(n):
		print(gevent.getcurrent(),i)
		time.sleep(0.5)

def f2(n):
	for i in range(n):
		print(gevent.getcurrent(),i)
		time.sleep(0.5)

def f3(n):
	for i in range(n):
		print(gevent.getcurrent(),i)
		time.sleep(0.5)

gevent.joinall([
	gevent.spawn(f1,5),
	gevent.spawn(f2,5),
	gevent.spawn(f3,5)
])