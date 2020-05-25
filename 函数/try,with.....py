# 生活不会突变，你要做的只是耐心和积累。人这一辈子没法做太多的事情，所以每一件尽力而为。
# -*- coding: utf-8 -*-

### try....except.....finally 语句中，含有 return的，执行顺序
##  存在 finally 语句时，代码一定会执行该语句，raise KeyError 时，程序进入 except 捕获
##  打印 key error，由于存在 finally ，会直接 返回 return 4 结束函数
##  不存在 finally ，会返回 return 2

def exe_try():
	try:
		print('code start')
		raise KeyError
		return 1
	
	except KeyError as e:
		print('key error')
		return 2
	
	else:
		print('other error')
		return 3
	
	finally:
		print('finally')
		return 4


if __name__ == '__main__':
	result=exe_try()
	print(result)


## 列表+，+=，extend（）

s=[1,2,3]
print(s+[5,7]) ## 创建新列表
print(s)   ## 原列表不变

## print(s+(2,8))   ## 报错，列表不能加元组

s+=(3,7)
print(s)   ## += 可以加元组
print()

## += 等价 extend（）

l=[7,8,9]
l.extend((4,7,9))
print(l)
