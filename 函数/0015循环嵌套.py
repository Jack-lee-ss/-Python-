# -*- coding: utf-8 -*-
## 嵌套for循环
for i in range(1,10):
	for j in range(1,i+1):
		s=i * j
		print('%d*%d=%-3d'%(j, i, s),end=' ')
	print()
	
print()
'''
for i in range(1,10):
	for j in range(1,10):
		if j<=i:
			s=i * j
			print('%d*%d=%-3d'%(j, i, s),end=' ')  ## %-3d:字符串右边3位填充空格。
	print()
print()
#### continue:只暂停本次循环，继续下次循环
l=[23,56,74,46,86,36,77]
s=0
for i in l:
	if i>40:
		continue   ## 大于40不继续执行
	s+=1
print('不超过40的数字个数有：%d'%s)

dict={'a':100,'b':345,'c':235,'d':654}
s=0
for i in dict.values():
	if i >300:
		continue
	s+=1
print('小于300数字的个数：%d'%s)
print()

### for ....else...
# n=int(input('输入一个大于2的数字：'))
# if n==2:
# 	print('%d是质数'%n)
# else:
# 	for i in range(2,n):
# 		if n%i==0:
# 			print('%d不是质数'%n)
# 			break
# 		else:
# 			print('%d是质数'%n)
# 			break

### for ....else...:跳出多层循环
count=0
s=[23,45,67,89,65,345,984,3.4,453,89,349,76,58]
for i in s:
	for j in range(100):
		if i==j:
			count+=1
			break
		else:
			continue
print('统计列表中元素在1-100内的数字个数：%d'%count)  ## 统计列表中元素在1-100内的数字个数，列表遍历统计完
print()

count=0
s=[234,454,674,89,65,345,984,3.4,453,89,34,76,38,90,33.4]
for i in s:
	for j in range(100):
		if i==j:
			break
	else:
		continue
	break
print('列表中第一个出现在1-100内的元素是: %d'%i)  ## 打印出列表中第一个出现在1-100内的元素

m=[]
s=[234,454,674,89,65,345,984,3.4,453,89,34,76,38,90,33.4]
for i in s:
	for j in range(100):
		if i==j:
			m.append(i)
			break
	else:
		continue
print('新列表:',m)
print()


### 跳出多层循环：
## 方法一：判断 a==x成立条件

s=[234,454,674,89,65,345,984,3.4,453,87,34,76,38,90,33.4]
x=0
a=int(input('输入数字: '))
print(a)
for i in s:
	for j in range(100):
		if i==j:
			if a==x:
				x+=1
				break
			else:
				x+=1
				continue
		else:
			continue
	if a==x:                  ## 判断 a==x成立条件
		break
	else:
		continue
print(i)

#### 方法二：函数加return
def	main():
	s = [234, 454, 674, 89, 65, 345, 984, 3.4, 453, 87, 34, 76, 38, 90, 33.4]
	x = 1
	a = int(input('输入数字: '))   ## 整型数字
	print(a)
	for i in s:
		for j in range(100):
			if i == j:
				print('.....')
				if a == x:         ## 数字之间比较
					print('$$$')
					x += 1
					print('----')
					return i       ## 函数体中，遇到return会自动返回值，跳出循环
				else:
					x+=1
					print('***')
					continue
			else:
				continue
		else:
			continue

if __name__== '__main__':
	s=main()
	print(s)

#### 方法三：break 语句
s = [234, 454, 674, 89, 65, 345, 984, 3.4, 453, 87, 34, 76, 38, 90, 33.4]
x = 1
a = int(input('输入数字: '))
print(a)
for i in s:
	for j in range(100):
		if i == j:
			if a == x:
				x += 1
				break
			else:
				x += 1
				continue
		else:
			continue
	else:
		continue
	break                  ### 此处 break 跳出外层循环
print(i)


#### 方法四：定义标记变量
s = [234, 454, 674, 89, 65, 345, 984, 3.4, 453, 87, 34, 76, 38, 90, 33.4]
x = 1
a = int(input('输入数字: '))
print(a)
flag=True                        ### 定义标记变量
for i in s:
	for j in range(100):
		if i == j:
			if a == x:
				flag=False
				x += 1
				break
			else:
				x += 1
				continue
		else:
			continue
	else:
		continue
		
	if not flag:
		break
print(i)
'''

#### while 循环
## 猜字游戏
answer=30
guess=0
while guess!=answer:
	guess=int(input('请猜1-100的数字= '))
	if guess > answer:
		print('请猜小一点')
	elif guess<answer:
		print('请猜大一点')
	else:
		print('答对了')

### 嵌套 while 循环
## 9 × 9
i=1
while i<=9:
	j=1
	while j<=i:
		s=i*j
		print('%d*%d=%-3d'%(j,i,s),end=' ')
		j+=1
	print()
	i+=1

### while break continue
# s = [234, 454, 674, 89, 65, 345, 984, 3.4, 453, 87, 34, 76, 38, 90, 33.4]
# x = 1
# a = int(input('输入数字: '))
# print(a)
# i=0
# while True:
# 	if s[i] in range(100):
# 		if a==i:
# 			print(s[i-1])
# 			break
# 		else:
# 			i+=1
# 			continue
# 	else:
# 		i+=1
# 		continue

