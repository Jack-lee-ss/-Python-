# -*- coding: utf-8 -*-
#### 生成器： yield 全面总结

## 简单yield的使用（几种调用方式）
## 每调用一次 next()，函数都会执行到yield处停止，等待下一次next，next次数超出限制就会抛出异常
def myfun(total):
    for i in range(total):
        yield i
m=myfun(4)
print(next(m))
print(next(m))
print(next(m))
print(next(m))
#print(next(m))   ## 出现异常
print()

## 2.循环调用
def myfun(total):
    for i in range(total):
        yield i
for i in myfun(4):
    print(i,end='')
print()

## 3.循环中调用next,用StopIteration捕获异常并退出循环
def myfun(total):
    for i in range(total):
        yield i
m = myfun(4)
while True:
	try:
		print(next(m))
	except StopIteration:
		break
print('============')

##### yield空:yield空相当于一个中断器，循环运行到这里会中断，用于辅助其他程序的执行。也可以理解成返回值是None.

def myfun(total):
	for i in range(total):
		print(i+1,end='')
		yield             ##  返回值是None
		
a=myfun(6)
for i in a:
	print(i,end='')
print()

### yield from ：遍历一个可以迭代的对象 yield from 相当于一个 for 循环
def myfun(total):
	for i in range(total):
		yield i
	yield from ['a', 'b', 'c']
m=myfun(6)
while True:
	try:
		print(next(m),end=' ')
	except StopIteration:
		break
print()
print('..................')

###  send与yield赋值:next相当于send(None).执行下一次循环
## send(None)
def myfun(total):
	for i in range(total):
		yield i
m=myfun(6)
while True:
	try:
		print(m.send(None),end=' ')
	except StopIteration:
		break
print()
print()

### send(i):send()表示向这个生成器中传入东西，有传入就得有变量接着，于是引出了yield赋值
def myfun(total):
	for i in range(total):
		print('***')
		r=yield i
		print(r,'+++')
		
m=myfun(6)
while True:
	try:
		print(m.send(None),'---',end=' ')
		print('$$$ ',end='')
		print(m.send(1),'===',end=' ')
	except StopIteration:
		break


#####  yield from 使用;
from itertools import chain
list=[1,2,3,4,5]
dict={
	'a':1111,
	'b':'abghh'
}
for value in chain(list,dict):   ## 打印出列表，或者字典键的元素
	print(value,end='')
print()
for value in chain(list,dict,range(3,9)):   ## 打印列表或者字典键在（3,9）范围的元素
	print(value,end='')

### yield from
from itertools import chain

list = [1, 2, 3, 4, 5]
dict = {
	'a': 1111,
	'b': 'abghh'
}


def my_chain(*args, **kwargs):
	for i in args:
		yield from i


for value in my_chain(list, dict, range(3, 9)):  ## 打印列表或者字典键在（3,9）范围的元素
	print(value, end='')
print()


######## yield from 可以遍历每一个可迭代对象中的元素，yield from后面加上可迭代对象，他可以把可迭代对象里的每个元素一个一个的yield出来。
def g1(i):
	yield i


def g2(i):
	yield from i


for value in g1(range(10)):
	print(value)

for value in g2(range(10)):
	print(value, end='')
print()


#### 1、调用方：调用委派生成器的客户端（调用方）代码；2、委托生成器：包含yield from表达式的生成器函数3、子生成器：yield from后面加的生成器函数。

def average_gen():  ## 子生成器
	t = 0
	count = 0
	average = 0
	while True:
		new_num = yield average
		count += 1
		t += new_num
		average = t / count


def proxy_gen():  ## 委托生成器
	while True:
		yield from average_gen()  ## yield from + 生成器


def main():  ## 调用方
	calc_average = proxy_gen()
	next(calc_average)
	print(calc_average.send(10))
	print(calc_average.send(20))
	print(calc_average.send(30))
	print(calc_average.send(40))


if __name__ == '__main__':
	main()
print()


## 委托生成器的作用是：在调用方与子生成器之间建立一个双向通道。调用方可以通过send()直接发送消息给子生成器，而子生成器yield的值，也是直接返回给调用方。


#### yield from前面看到可以赋值
def average_gen():  ## 子生成器
	t = 0
	count = 0
	average = 0
	while True:
		new_num = yield average
		if new_num is None:
			break
		count += 1
		t += new_num
		average = t / count
	print('------------')
	return t, count, average  ## 每一次return，都意味着当前协程结束


def proxy_gen():  ## 委托生成器
	while True:
		## 只有子生成器结束了（return）了，yield from 左边变量才会赋值，后面代码才执行。
		t, count, average = yield from average_gen()  ## yield from + 生成器
		print('计算完毕！\n总共传入{}个数值，总和：{}，平均数：{}'.format(count, t, average))


def main():  ## 调用方
	calc_average = proxy_gen()
	next(calc_average)
	print(calc_average.send(10))
	print(calc_average.send(20))
	print(calc_average.send(30))
	print(calc_average.send(40))
	calc_average.send(None)  ## 结束协程


if __name__ == '__main__':
	main()