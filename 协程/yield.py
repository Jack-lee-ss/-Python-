# 生活不会突变，你要做的只是耐心和积累。人这一辈子没法做太多的事情，所以每一件尽力而为。
# -*- coding: utf-8 -*-
'''
	并发：一个时间内，有几个程序在同一个cpu上运行，但是任意时刻只有一个程序在cpu上运行
	并行：在任意时刻点上，有多个程序同时运行在多个cpu上，并行数=CPU数。
	
	同步：代码调用io操作时，必须等待io操作完成后才能返回调用方式
	异步：不必等io操作完成就可以返回调用方式

'''
## 生成器函数：yield
#斐波拉西数列
def fib(index):
	if index<=2:
		return 1
	else:
		return fib(index-1)+fib(index-2)
print(fib(8),'\n')

l=[]
def fib2(x):
	a, b, c = 0, 0, 1
	while a < x:
		l.append(c)
		b, c = c, b + c
		a += 1
	return l
print(fib2(10),'\n')


def fib1(x):
	a,b,c=0,0,1
	while a<x:
		yield c
		b,c=c,b+c
		a+=1

for i in fib1(10):
	print(i)


# 生成器读取大文件：
# 具有固定分割符的文件，只有一行(有{|}分隔符，结尾无分隔符)，无法使用 f.readlines() 或者 for line in f:

def myreadlines(f,newline):
	buff=""
	while True:
		while newline in buff:
			pos=buff.index(newline)  ## index可以直接查找到字符串里面某个字符的位置。
			yield buff[:pos]          # 返回 myreadlines() 函数
			buff=buff[pos+len(newline):]

		chunk=f.read(1024)

		if not chunk:    ## 读取不到字节，表示到了文件结尾
			yield buff
			break
		buff+=chunk

with open('input.txt') as f:
	for line in myreadlines(f,"{|}"):
		print(line)


# send():
def gen_func(value):
	while True:
		html=yield
		print(str(html) +value)

l=[1,2,4,5,7]
gen=gen_func("https://www.baidu.com")

u=gen.send(None)  ## 启动生成器

for i in l:
	gen.send(i)




#### 分割不固定分隔符的文件

def function(t,l):
	return l[t]

def myreadlines(f,l):
	buff = ""
	t=0
	newline = function(t,l)
	while True:
		while newline in buff:
			pos = buff.index(newline)  ## index可以直接查找到字符串里面某个字符的位置。
			yield buff[:pos]  # 返回 myreadlines() 函数
			buff=buff[pos+len(newline):]
			if newline != l[len(l)-1]:
				t+=1
				newline = function(t,l)

		chunk = f.read(400)
		if not chunk:  ## 读取不到字节，表示到了文件结尾
			yield buff
			break
		buff += chunk

l = ['(1)', '(2)', '()', '(3)', '(4)','(5)','(6)']
with open('split.txt') as f:
	for line in myreadlines(f,l):
		print(line)

# import  re
# s="432432fgg(1)4u2309hfehhfdshsd(2)f293u238hfedshf()fjisdj(3)23904u2039f0dshf(4)2[u23hfuhdsufnsd"
# f=re.findall(r'\(.*?\)',s)
#
# def ac(s,f):
# 	l=[]
#
#
#
# print(ac(s,f))


## yield from
def sales_sum(name):
	total=0
	nums=[]
	while True:
		x=yield
		print(name+"销量: ", x)
		if not x:
			break
		total+=x
		nums.append(x)
	return total,nums

if __name__=="__main__":
	my_gen=sales_sum("百度手机")
	my_gen.send(None)
	my_gen.send(1200)
	my_gen.send(5003)
	try:
		my_gen.send(None)
	except StopIteration as e:
		result=e.value   ## StopIteration: (6203, [1200, 5003]) 字典或json数据
		print(result)


## async 和 await --------------- 原生协程
async def downloader(url):
	return "bobby"

async def download_url(url):
	html=await downloader(url)
	return html

if __name__=="__main__":
	gen=download_url("https://www.baidu.com")
	try:
		gen.send(None)
	except StopIteration as e:
		result = e.value
		print(result)


