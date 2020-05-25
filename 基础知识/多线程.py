# # -*- coding: utf-8 -*-
## 可迭代对象：生成器，列表，字典，字符串
"""
import time ,threading

def bank_handle(semaphore):  ## 定义银行相关处理业务
	if semaphore.acquire():  ## 常识获取信号量，如果没有获取就等待
		print('[%s]资源抢占成功，开始办理个人相关业务。。。'%(threading.current_thread().name))
		time.sleep(3) ## 模拟业务办理时间
		semaphore.release() # 释放锁定
def main():
	semaphore=threading.Semaphore(4)  ## 获取信号量同步锁，一次性4个工作量
	thread_list=[threading.Thread(target=bank_handle,args=(semaphore,),name="银行客户 - %s"% item) for item in range(10)]
	for thread in thread_list:
		thread.start()

if __name__ == '__main__':
	main()  ## 调用主函数
"""
## 可迭代对象：生成器，列表，字典，字符串
######## 多协程  send ，yield

# def procuder(cons):
# 	info=None       ## 生产数据
# 	cons.send(info)  # 必须先发送一个None数据
# 	for item in range(10):
# 		if item% 2 == 0:
# 			info='title = 小李老师，content = 软件技术讲师'
# 		else:
# 			info='title = yootk.content = www.yutk.com'
# 		cons.send(info) ## 数据发送给消费者
#
# def consumer():
# 	while True:
# 		receive=yield  # 等待数据接收
# 		print('[消费者]%s'%receive) ## 消费者输出信息
#
# def main():
# 	con=consumer()
# 	procuder(con)
#
# if __name__=='__main__':
# 	main()


#### yield from 语法
# from itertools import chain
# list=[1,2,3,4,5]
# dict={
# 	'a':1111,
# 	'b':'abghh'
# }
# for value in chain(list,dict):   ## 打印出列表，或者字典键的元素
# 	print(value,end='')
# print()
# for value in chain(list,dict,range(3,9)):   ## 打印列表或者字典键在（3,9）范围的元素
# 	print(value,end='')

### yield from
from itertools import chain
list=[1,2,3,4,5]
dict={
	'a':1111,
	'b':'abghh'
}
def my_chain(*args,**kwargs):
	for i in args:
		yield from i
		
for value in my_chain(list,dict,range(3,9)):   ## 打印列表或者字典键在（3,9）范围的元素
	print(value,end='')
print()

######## yield from 可以遍历每一个可迭代对象中的元素，yield from后面加上可迭代对象，他可以把可迭代对象里的每个元素一个一个的yield出来。
def g1(i):
	yield i

def g2(i):
	yield from i

for value in g1(range(10)):
	print(value)

for value in g2(range(10)):
	print(value,end='')
print()

#### 1、调用方：调用委派生成器的客户端（调用方）代码；2、委托生成器：包含yield from表达式的生成器函数3、子生成器：yield from后面加的生成器函数。

def average_gen():   ## 子生成器
	t=0
	count=0
	average=0
	while True:
		new_num=yield average
		count+=1
		t+=new_num
		average=t/count

def proxy_gen():	## 委托生成器
	while True:
		yield from average_gen()  ## yield from + 生成器

def main():         ## 调用方
	calc_average=proxy_gen()
	next(calc_average)
	print(calc_average.send(10))
	print(calc_average.send(20))
	print(calc_average.send(30))
	print(calc_average.send(40))

if __name__==  '__main__':
	main()
print()

## 委托生成器的作用是：在调用方与子生成器之间建立一个双向通道。调用方可以通过send()直接发送消息给子生成器，而子生成器yield的值，也是直接返回给调用方。


#### yield from前面看到可以赋值
def average_gen():   ## 子生成器
	t=0
	count=0
	average=0
	while True:
		new_num=yield average
		if new_num is None:
			break
		count+=1
		t+=new_num
		average=t/count
	print('------------')
	return t,count,average  ## 每一次return，都意味着当前协程结束

def proxy_gen():	## 委托生成器
	while True:
		## 只有子生成器结束了（return）了，yield from 左边变量才会赋值，后面代码才执行。
		t,count,average = yield from average_gen()  ## yield from + 生成器
		print('计算完毕！\n总共传入{}个数值，总和：{}，平均数：{}'.format(count,t,average))

def main():         ## 调用方
	calc_average=proxy_gen()
	next(calc_average)
	print(calc_average.send(10))
	print(calc_average.send(20))
	print(calc_average.send(30))
	print(calc_average.send(40))
	calc_average.send(None)      ## 结束协程

if __name__==  '__main__':
	main()


### async await
async def downloader(url):
	return 'boby'

async def download_url(url):
	html=await downloader(url)
	return html

if __name__== '__main__':
	a=download_url('https://www.baidu.com')
	a.send(None)