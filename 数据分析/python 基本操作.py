#### ============ os.system函数 ======================
## 使用os库的 system 函数 调用其它程序
# import os
# ### 使用 wget 下载，默认下载路径在 该程序代码所在位置
# cmd = r'D:\data\wget\wget.exe http://mirrors.sohu.com/nginx/nginx.zip'
# os.system(cmd)
# print('---下载完毕---')

### 比如，我们安装测试环境的时候， 安装包的名称 由于 版本号不同，是经常会变化的。可以运行时，让用户输入版本，然后再填入命令行字符串中。
'''
version = input('请输入安装包版本:')
cmd = fr'd:\tools\wget http://mirrors.sohu.com/nginx/nginx-{version}.zip'
os.system(cmd)

print('下载完毕')

'''
### os.system 函数调用外部程序的时候，必须要等被调用程序执行结束，才会接着往下执行代码。 否则就会一直等待。

##  subprocess 模块(略过)

## 异常值处理
# 在命令行窗口 运行 Python 解释器交互命令行时会输入错误类型值，如果我们在编码的时候，就预料到了某些代码运行时可能出现某些异常，就可以使用 try...except... 这样的方法来捕获和处理异常，except 后面缩进的代码 就是对这种类型错误 的一种处理。
# while True:
#     try:
#         miles = input('请输入英里数:')
#         km = int(miles) * 1.609344
#         print(f'等于{km}公里')
#     except ValueError:
#         print('你输入了非数字字符')
#
# # 如果我们开发程序的时候，估计某个代码段中可能出现好几种类型的异常，可以使用多个except 代码段，分别捕获多种类型的异常。
# import traceback
#
# while True:
# 	try:
# 		choice = input('输入你的选择:')
# 		if choice == '1':
# 			100/0
# 		elif choice == '2':
# 			[][2]
# 	except ZeroDivisionError:
# 		print ('出现 ZeroDivisionError')
# 	except IndexError  :
# 		print ('出现 IndexError')
# 	break
#
# #### 所有异常值都是标准库里面的 Exception 类，所以在处理发生不可知的异常对象时，可以将异常对象值赋给 as 后的变量。因为所有的异常都是 Exception 的子类。 所以 Exception能匹配所有类型的异常
# try:
# 	100/0
# except  Exception  as e:
# 	print(f'异常对象信息:{e}','\n')
#
# ##还有一种更简洁的写法，也可以匹配所有类型的异常，如下所示.except 后面没有写异常的类型，也表示匹配所有的异常。
#
# try:
# 	100/0
# except:
# 	print('未知异常:','怎么办','\n')
#
#
# ## 如果我们想知道异常的详细信息，可以使用traceback模块
# ## format_exc函数:可以显示异常的信息 和 异常产生处的函数调用栈的信息
# try:
# 	100/0
# except:
# 	print(traceback.format_exc())
#
#
# ######  基本数据操作
# 合并两个列表
# import openpyxl
# from pandas import Series
#
# a=[1,2,3,]
# b=[4,6,'d','_']
# c=[3,6,'%']
# print(a+b+c)
#
# # 合并字典:如果有重复的key，会被字典y中的内容取代
# x = {'a':1, 'b': 2}
# y = {'b':10, 'c': 11}
# x.update(y)
# print(x)
#
# ###### 去重复数方法
# ## 如果我们想将合并后的内容放到一个新的字典对象里面， 而不去修改x，y的内容
# z = dict(list(x.items()) + list(y.items()))
# print(z)
#
# ## set():set集合的元素是唯一的、不重复的,但原列表的元素顺序可能会发生改变
# a=[2,6,9,8,9,3,8,3,9]
# b=list(set(a))
# print(b)
# print(a,'\n')
#
# ## 使用Series的unique方法
# a=[2,6,9,8,9,3,8,3,9]
# b=Series(list(a))
# print(list(b.unique()))
#
# ### 从字典中过滤元素：将武力值 在 95 以上的 武将 放到一个新的字典中
# guys = {
#     '关羽' : 96,
#     '张飞' : 96,
#     '赵云' : 97,
#     '马超' : 96,
#     '黄忠' : 94,
#     '魏延' : 90,
#     '马岱' : 82,
# }
# toughGuys = {guy:level for guy,level in guys.items() if level > 95}
# print(toughGuys)
#
# ## 在Excel中写入字典数据
# s=[{'译名': '决X中途岛/中途岛战役/中途岛海战',
#    '片名': '中间的way',
#    '年代': '2019',
#    '产地': '中国/美国',
#    '类别': '战争/历史',
#    '语言': '英语',
#    '字幕': '中文字幕',
#    'IMDb评分': '6.9/10 from 12377 用户',
#    '视频尺寸': '1920 x 798',
#    '片长': '138 Mins',
#    '导演': '罗兰·艾默里奇 Roland Emmerich',
#    '主演': '伍迪·哈里森 Woody Harrelson 帕特里克·威尔森 Patrick Wilson 卢克·伊万斯 Luke Evans 艾德·斯克林 Ed Skrein 丹尼斯·奎德 DennisQuaid 曼迪·摩尔 Mandy Moore 亚历山大·路德韦格 Alexander Ludwig 艾伦·艾克哈特 Aaron Eckhart 达伦·克里斯 Darren Criss'},
#   {'译名': '途岛海战',
#    '片名': '间的way战争',
#    '年代': '2019',
#    '产地': '中国/美国',
#    '类别': '战争/历史',
#    '语言': '英语',
#    '字幕': '中文字幕',
#    'IMDb评分': '3.8/10 from 1234 用户',
#    '视频尺寸': '1920 x 798',
#    '片长': '138 Mins',
#    '导演': '肯尼迪 Roland Emmerich',
#    '主演': '帕特里克·威尔森 Patrick Wilson 卢克·伊万斯 Luke Evans 艾德·斯克林 Ed Skrein 丹尼斯·奎德 DennisQuaid 曼迪·摩尔 Mandy Moore 亚历山大·路德韦格 Alexander Ludwig 艾伦·艾克哈特 Aaron Eckhart 达伦·克里斯 Darren Criss伍迪·哈里森 Woody Harrelson '},
#   {'译名': '赏花点',
#    '片名': 'Python',
#    '年代': '2013',
#    '产地': '美国',
#    '类别': '战争/历史/爱情',
#    '语言': '韩语',
#    '字幕': '英文字幕',
#    'IMDb评分': '8/10 from 1234 用户',
#    '视频尺寸': '1920 x 798',
#    '片长': '136 Mins',
#    '导演': '乔治·卢卡斯 Roland Emmerich',
#    '主演': '卢克·伊万斯 Luke Evans 艾德·斯克林 Ed Skrein 丹尼斯·奎德 DennisQuaid 曼迪·摩尔 Mandy Moore 亚历山大·路德韦格 Alexander Ludwig 艾伦·艾克哈特 Aaron Eckhart 达伦·克里斯 Darren Criss伍迪·哈里森 Woody Harrelson 帕特里克·威尔森 Patrick Wilson'},
#   {'译名': '忙点',
#    '片名': 'JS',
#    '年代': '2012',
#    '产地': '美国',
#    '类别': '战争/历史/爱情',
#    '语言': '日语',
#    '字幕': '西班牙文字幕',
#    'IMDb评分': '8.8/10 from 1234 用户',
#    '视频尺寸': '1920 x 798',
#    '片长': '136 Mins',
#    '导演': '威尔史密斯 Roland Emmerich',
#    '主演': '艾德·斯克林 Ed Skrein 丹尼斯·奎德 DennisQuaid 曼迪·摩尔 Mandy Moore 亚历山大·路德韦格 Alexander Ludwig 艾伦·艾克哈特 Aaron Eckhart 达伦·克里斯 Darren Criss伍迪·哈里森 Woody Harrelson 帕特里克·威尔森 Patrick Wilson 卢克·伊万斯 Luke Evans'}
#    ]
# ######   三种排列方式输入列表中的字典数据
# book=openpyxl.Workbook()
# sh=book.active
# sh.title='最新电影信息'
# sh1=book.create_sheet('movies1',0)
# sh2=book.create_sheet('movies2',1)
#
# ### 第一种
# r=0
# for x in s:
# 	c=0
# 	row = r
# 	col = c
# 	if x == s[0]:
# 		for i,j in x.items():
# 			book['movies1'].cell(row+1,col+1).value=i
# 			book['movies1'].cell(row+2,col+1).value=j
# 			col+=1
# 	elif x!=s[0]:
# 		for i, j in x.items():
# 			book['movies1'].cell(row+3,col+ 1).value = j
# 			col+=1
# 		r+=1
#
# #####  第二种
# row=2
# book['movies2'].cell(1, 1).value = '详情列'
# book['movies2'].cell(1, 2).value = '数据'
# for x in s:
# 	for i,j in x.items():
# 		book['movies2'].cell(row, 1).value = i
# 		book['movies2'].cell(row, 2).value = j
# 		row+=1
# 	row+=1
#
# #### 第三种
# row=1
# for x in s:
# 	col = 1
# 	for i,j in x.items():
# 		book['最新电影信息'].cell(row,col).value=i
# 		book['最新电影信息'].cell(row+1,col).value=j
# 		col+=1
# 	row+=3
#
# book.save('电影信息.xlsx')
#
# info_list = [
#     {'name':'zhao','age':'22','hight':'171'},
#     {'name':'qian','age':'23','hight':'165'},
#     {'name':'sun','age':'24','hight':'148'},
#     {'name':'li','age':'25','hight':'166'}]
# for i in s:
# 	## 遍历列表中字典的各对键和值
# 	print('name:%s\nage:%s\nhight:%s'%(i['name'],i['age'],i['hight']))


####  文本读取与写入
# 本文读写的文件，都是指 文本文件，不是视频，图片。读写文本文件， 首先通过内置函数open 打开一个文件，open函数会返回一个对象，我们可以称之为文件对象。文件的打开，分为 文本模式 和 二进制模式。open(路径，模式，编码)
## 相对路径：当前工作目录（代码）下的文件；绝对路径：从一个磁盘根目录下开始
## 打开模式：r 只读文本模式打开；w 创建一个新文件写入内容，或者清空某个文本文件重新写入内容； a 从某个文件末尾添加内容
## 编码模式：字符编解码
# 指定编码方式为 utf8
import re
#
# f = open('tmp.txt','w',encoding='utf8')
#
# # write方法会将字符串编码为utf8字节串写入文件
# f.write('白月黑羽：祝大家好运气')
#
# # 文件操作完毕后， 使用close 方法关闭该文件对象
# f.close()
#
# # 指定编码方式为 gb2312
# f = open('tmpp.txt','w',encoding='gb2312')
#
# # write方法会将字符串编码为gb2312字节串存入文件中
# f.write('白月黑羽：祝大家好运气')
#
# # 文件操作完毕后， 使用close 方法关闭该文件对象
# f.close()
#
# #####  在文件末尾添加新的内容，而不是删除掉原来的内容重新写,用追加模式 a 打开文件
# # a 表示 追加模式 打开文件
# f = open('tmpp.txt','a',encoding='gb2312')
# f.write('白月黑羽再次祝大家 ：good luck')
# f.close()
#
# ##### 读入文本
# # 指定编码方式为 gbk，gbk编码兼容gb2312
# f = open('tmpp.txt','r',encoding='gbk')
#
# # read 方法会在读取文件中的原始字节串后， 根据上面指定的gbk解码为字符串对象返回
# content = f.read()
#
# # 文件操作完毕后， 使用close 方法关闭该文件对象
# f.close()
#
# # 通过字符串的split方法获取其中用户名部分
# name = content.split('：')[0]
# print(name)
#
# ### 读取文件的部分字节：
# ## read函数有参数size，读取文本文件的时候，用来指定这次读取多少个字符
# ## 先创建一个文本
# f=open('abc.txt','w')
# ## 因为都是 英文字符，基本上所以的编码方式都兼容ASCII，可以无须指定encoding参数,读取文本时可以不指定编码方式
# s="""
# hello
# cHl0aG9uMy52aXAgYWxsIHJpZ2h0cyByZXNlcnZlZA==
# """
# ## 写入一个字符串
# f.write(s)
# f.close()
#
# ## 读该文件
# f=open('abc.txt')
# read=f.read(5)
# print(read)
#
# ## 再读4个字符，从上次读完的地方继续；注意：换行符\n也是一个字符串，但不显示
# read=f.read(4)
# print(read)
#
# ## 不加参数，读取剩下所有内容
# read=f.read()
# print(read)
# print('--------------------------','\n')
#
# ### 读取文件行内容
# ##  readlines方法，该方法会返回一个列表。列表中的每个元素依次对应文本文件中每行内容.
# f = open('abc.txt')
# linelist = f.readlines()
# f.close()
# for line in linelist:
# 	### 每一行读取完会自动换行，列表的每个元素对应的字符串 最后有一个换行符
# 	### 但print()会自动打印换行，所以，行之间会空一行。
#     print(line,'\n')
#
# ##  如果你不想要换行符，可以使用字符串对象的splitlines方法
# f = open('abc.txt')
# content = f.read()   # 读取全部文件内容
# f.close()
#
# # 将文件内容字符串 按换行符 切割 到列表中，每个元素依次对应一行
# linelist = content.splitlines()
# for line in linelist:
# 	print(line)
	
####  注：查看某一个代码用法：①可以先按住 Ctrl，在鼠标点到该代码字符上，出现蓝色线，点击即可看到其用法。②鼠标指到该函数字符，按住 Ctrl+shift+i 即可参看该用法。③指在该字符上，按住 ctrl+b 查看其用法。

### 修改自定义变量：对于大量的自定义变量，如果需要修改，手动会很麻烦，可以选中该变量名，右键 refactor --> rename ;修改变量名，再点击 refactor ，进入页面后，点击左下方 Do refactor,即可修改完。

### 文本换行操作
## 运算符号换行不影响代码运行
print(1+2+3+5+6+7+1
	  +2+3+5+6+7+1
	  +2+3+5+6+7)

## \ ：一行变多行
print('中共中央总书记、国家主席、中央军委主席习近平\
10日在北京调研指导新型冠状病毒肺炎疫情防控工作时强调，\
当前疫情形势仍然十分严峻，各级党委和政府要坚决贯彻党\
中央关于疫情防控各项决策部署，坚决贯彻坚定信心、\
同舟共济、科学防治、精准施策的总要求，再接再厉、\
英勇斗争，以更坚定的信心、更顽强的意志、更果断的措施，\
紧紧依靠人民群众，坚决把疫情扩散蔓延势头遏制住，\
坚决打赢疫情防控的人民战争、总体战、阻击战')

## 单行合并代码
a=1;b=2;c=3;print(a,b,c)



