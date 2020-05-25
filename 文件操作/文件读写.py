# -*- coding: utf-8 -*-
## 文本读取，不可写
'''
## 读取整个文本
f=open(r'F:\python代码\Python 基本操作\文件操作\歌词.txt','r',encoding='gbk')
## 读取前5行
for i in range(5):
	print(f.readline().strip())
print('=============')

## 读取剩余文本
data=f.read()
print(data.strip())
f.close()
print('-------------------')

### 不读取特定行（低效率）
"""
f=open(r'F:\python代码\Python 基本操作\文件操作\歌词.txt','r',encoding='gbk')
for index,line in enumerate(f.readlines()):
	if index==8:   ## 第8行不打印
		continue
	print(line.strip())
"""
### 高效率
f=open(r'F:\python代码\Python 基本操作\文件操作\歌词.txt','r',encoding='gbk')
count=0
for line in f:    ## f：句柄
	if count==9:  ## 只读前九行
		break
	count+=1
	print(line.strip())
f.close()
print()
print('+++++不读第九行++++++')
print()
f=open(r'F:\python代码\Python 基本操作\文件操作\歌词.txt','r',encoding='gbk')
count=0
for line in f:    ## f：句柄
	if count==9:  ## 不读第九行
		count+=1
		continue
	print(line.strip())
	count+=1
f.close()
print()
print('------从第十行开始读-----')
print()
f=open(r'F:\python代码\Python 基本操作\文件操作\歌词.txt','r',encoding='gbk')
count=0
for line in f:    ## f：句柄
	if count<=9:  ## 不读第九行
		count+=1
		continue
	print(line.strip())
	count+=1
f.close()
print('======')

### f.tell():记录字节数
f=open(r'F:\python代码\Python 基本操作\文件操作\歌词.txt','r',encoding='gbk')
print(f.tell())      ## 未读则没有字节
print(f.readline())
print(f.tell())      ## 读一段后，一段的字节数

f.seek(0)    ## 回到开始
print(f.readline())
# f.seek(10,0)
# print(f.readline())
print(f.encoding)
print(f.seekable())
f.close()

import sys,time
for i in range(5):
	sys.stdout.write('愿你在尘世获得幸福\n')
	sys.stdout.flush()   ## 强制刷新缓冲区，立刻进行打印
	time.sleep(0.2)

# f=open(r'F:\python代码\Python 基本操作\文件操作\歌词.txt','r')
# f.seek(1,0)
# print(f.readline())



## 写内容    'w':创建新文件，如果之前有文件，则删除源文件在创建
f=open(r'F:\python代码\Python 基本操作\文件操作\打油诗.txt','w',encoding='utf-8')
f.write('窗前明月光,疑是地上霜.\n')
f.write('举头望明月,低头思故乡.\n')
f.close()

## 追加文件，在之前写的基础上添加内容
f=open(r'F:\python代码\Python 基本操作\文件操作\打油诗.txt','a',encoding='utf-8')
f.write('\n-----------武汉加油!----------')
f.close()
'''

### 上下文管理:打开两个文件
# with open(r'F:\python代码\Python 基本操作\文件操作\打油诗.txt','r',encoding='utf-8') as f1,\
# 	open(r'F:\python代码\Python 基本操作\文件操作\歌词.txt','r',encoding='gbk') as f2:
# 	for line in f1:
# 		print(line)
# 	print()
# 	for line in f2:
# 		print(line)

import json

b={'a':1,'b':2,'c':3,'d':4,'f':5}
f=open('./example.txt','w',encoding='utf-8')
s=json.dumps(b)
f.write(s)
print(type(s))
print(s)
f.close()

f=open('./example.txt','w',encoding='utf-8')
c=json.loads(s)
if c['b']:
	c.pop('b')and c.pop('a')
print(c)
print(type(c))



