# -*- coding: utf-8 -*-
import sys
print(sys.getdefaultencoding())  ### 查看默认编码

s=u'你好'
print(s.encode())  ## 二进制编码
print(s.encode().decode('gbk'))  ### 将二进制编码解码成 'gbk'
print(s.encode().decode('utf-8')) ## 将二进制编码解码成 'utf-8'

print('===========')

### python3里面，字符串要先encode手动指定其为某一编码的字节码之后，才能decode解码

print(type(s.encode('utf-8').decode('utf-8')))   ## str 转化为 unicode
print(s.encode('utf-8').decode('utf-8'))
print(s.encode('gbk'))
print(s.encode('utf-8').decode('unicode_escape'))
print(s.encode('gbk').decode('gbk'))

a=b'\xc4\xe3\xba\xc3'
print(a.decode('gbk'))
print(a.decode('unicode_escape'))
print()

######  异常处理
def division(x,y):
	try:
		result=x/y			    ## 未发生异常时直接打印结果
	except ZeroDivisionError:
		print('除数不可为零')   ## 发生异常时，打印原因
	
	else:
		return result           ## 发生异常的处理结果

print(division(10,4))
print(division(2,0))
print()

#### 处理文件找不到
def wordNum(f):
	try:
		with open(fn,'r',encoding='gbk') as f:
			data=f.read()
	except FileNotFoundError:
		print('找不到 %s文件'%fn)
	else:
		word=data.split()   ## 文章转化为列表
		print('文字数是：',len(word))
	
fn='./歌词.txt'
wordNum(fn)
print('===================')

### 捕捉多种异常
def division(x, y):
	try:
		result = x / y  ## 未发生异常时直接打印结果
	except (ZeroDivisionError,TypeError):
		print('除数不可为零或者类型错误')  ## 发生异常时，打印原因
	
	else:
		return result  ## 发生异常的处理结果

print(division(10, 4))
print()
print(division(2, 0))
print()
print(division('a','b'))
print('---------------------')

## 捕捉内置错误:
def division(x, y):
	try:
		result = x / y  ## 未发生异常时直接打印结果
	except (ZeroDivisionError, TypeError) as e:
		print(e)  ## 发生异常时，打印原因
	
	else:
		return result  ## 未发生异常的正常处理结果
	
print(division(10, 4))
print()
print(division(2, 0))
print()
print(division('a', 'b'))
print('+++++++++++++++++++++++')

### 捕捉所有异常：
def division(x, y):
	try:
		result = x / y  ## 未发生异常时直接打印结果
	except :
		print('一般异常')  ## 发生异常时，打印原因
	
	else:
		return result  ## 发生异常的处理结果

print(division(10, 4))
print()
print(division(2, 0))
print()
print(division('a', 'b'))
print()
print('************************')
########  验证密码长度
def passWord(pwd):
	pwd_len=len(pwd)
	if pwd_len>8:
		raise Exception('密码长度过长')
	elif pwd_len<8:
		raise Exception('密码长度不够')
	else:
		print('密码长度正确')

s=['aaaaabbbb','11234254','1234dg']
for pwd in s:
	try:
		passWord(pwd)
	
	except Exception as e:
		print('密码长度错误：',str(e))
		
	finally:                           ## 无论是否有异常，一定执行的操作
		print('---任务结束---')