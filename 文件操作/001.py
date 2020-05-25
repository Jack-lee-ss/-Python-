### 文本换行操作
## 运算符号换行不影响代码运行
import os
import time

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


### OS 模块

#获取当前代码所在目录
# f=open('text001.csv','w',encoding='gbk')
# f.write('Python学习')
# f.close()
a=os.getcwd()
print(a)

# 改变当前工作目录
path='D:\data'
os.chdir(path)
a=os.getcwd()
print(a)

#列举额当前文件的文件名.返回文件夹和文件构成的列表 '.'代表当前目录；'..'代表上一级目录
a=os.listdir('F:\python代码\数据分析')
print(a,'\n')

## 由于上面已经改变了文件夹位置，现在在path='D:\data'
b=os.getcwd()
## ./:代表当前文件夹
c=os.listdir('./')
print(c)
## ../:代表当前文件夹上级的文件夹;  ../../:上层的上层，以此类推。
c=os.listdir('../')
print(c,'\n','-------------------')

# 创建单个文件夹，不返回数值，如果该目录已存在，就抛出异常。
os.mkdir('F:\python代码\Python 基本操作\doc')
## 删除单个空文件夹
os.rmdir('F:\python代码\Python 基本操作\doc')

# 一般创建文件夹，可假设不存在，再创建。
if not os.path.exists('F:\python代码\Python 基本操作\doc11'):
	os.mkdir('F:\python代码\Python 基本操作\doc11')

# 递归船舰多层目录,创建多层文件夹
os.makedirs('F:/python代码/Python 基本操作/a/b/c')
# 递归删除空文件夹
os.removedirs('F:/python代码/Python 基本操作/a/b/c')

# 创建文件,创建文件后要关闭，不然无法删除，文件正在打开使用中。
f=open('F:/python代码/Python 基本操作/123.txt','w')
f.close()
# 删除文件
os.remove('F:/python代码/Python 基本操作/123.txt')

# 将文件或者文件夹名称 old重新命名为new
os.rename('F:/python代码/Python 基本操作/doc11','F:/python代码/Python 基本操作/doc1123')
os.rmdir('F:/python代码/Python 基本操作/doc1123')

# 运行系统shell命令:出现乱码解决方法：File->Settings->Editor->File Encodings 把Global Encoding设置成 GBK 即可。
# a=os.system('dir d:')
# print(a)
# a=os.system('ping www.baidu.com')
# print(a)

## 获取系统环境变量,返回变量信息 字符串
# a=os.getenv('path')
# print(type(a))
# 切割变量信息，返回列表字符串
# a=a.split(':')
# print(a,'\n''==============')

# putenv:设置环境变量，但一般不起效果,它只处理代码，不改变系统
# os.environ：专门处理环境变量
# a=os.environ
# 包括 path 在内的其他变量一起获取，返回一个字典组成的元组。
# print(a,'\n')
# 只提取path
# print(a['path'],'\n')
# 添加环境变量
# os.environ['path']=os.environ['path']+';'+'F'
# print(os.environ['path'])
# print('=============')


## os 模块中常见的值
# 返回 . 指代当前目录（'.'）
print(os.curdir)
# 返回 .. 指代上一级目录
print(os.pardir)
# nt:windows操作系统；posix:liunx 系统
print(os.name)
# 输出操作系统特定的路径分隔符（Win下为'\';Linux下为'/'）
print(os.sep)
# 当前平台使用的行终止符（Win下为'\r\n';Linux下为'\n'）
print(os.linesep)
# repr() 函数将对象转化为供解释器读取的形式
print(repr(os.linesep),'\n')

###### os.path 模块：os.path模块是不属于os模块的，这是单独出来的os.path模块。
## os.path.abspath():将相对路径转化为绝对路径
path='../../text001'
a=os.path.abspath(path)
print(a)

# 去掉目录路径，单独返回文件名
print(os.path.basename(path))

# 去掉文件名，单独返回路径
print(os.path.dirname(path))

#将path1，path2各个部分组成一个路径名,但不会创建一个该路径的文件。
path1='F:/python代码/Python 基本操作/'
path2='data/a.txt'
a=os.path.join(path1,path2)
print(a)

# 分割文件名与路径，返回（f_path,f_name)元组。如果完全使用目录，他也会将最后一个目录作为文件名分离，且不会判断文件或者目录是否存在。
a=os.path.split('F:/python代码/Python 基本操作')
print(a)

# #分离文件名和扩展名，返回元组.获取文件后缀。
a=os.path.splitext('F:/python代码/Python 基本操作/123.txt')
print(a)

# 返回指定真实文件的尺寸，单位是字节,而不是文件夹大小
a=os.path.getsize('F:/python代码/Python 基本操作/text001.csv')
print(a)

# 判断制定路径是否存在且是一个目录,返回布尔值
print(os.path.isdir('F:/python代码/Python 基本操作/'))

# 判断制定路径是否存在且是一个文件
print(os.path.isfile('F:/python代码/Python 基本操作/'))

# 判断指定路径是否存在且是一个符号链接
print(os.path.islink('F:/python代码/Python 基本操作/'))

# 返回指定文件最近的访问时间（浮点型秒数，可用time模块的gmtime()或者localtime()函数换算）
print(os.path.getatime('F:/python代码/Python 基本操作/'))

# 返回指定文件创建时间（浮点型秒数，可用time模块的gmtime()或者localtime()函数换算）
print(os.path.getctime('F:/python代码/Python 基本操作/'))

# 返回指定文件最近修改时间（浮点型秒数，可用time模块的gmtime()或者localtime()函数换算）
print(os.path.getmtime('F:/python代码/Python 基本操作/'))
print(time.gmtime(os.path.getmtime('F:/python代码/Python 基本操作/')))

#判断制定路径（目录或者文件）是否存在 ,返回布尔值
a=os.path.exists('F:/python代码/Python 基本操作/')
print(a)

#判断指定路径是否为绝对路径，布尔值返回
a=os.path.isabs('F:/python代码/Python 基本操作/')
print(a)

#判断path1和path2两个路径是否指向同一个文件
# pat2='F:/python代码/Python 基本操作/text001.csv'
# pat1='./text001.csv'
# print(os.path.getsize(pat1))
# a=os.path.samefile(pat1,pat2)
# print(a)
