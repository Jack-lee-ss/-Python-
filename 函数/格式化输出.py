# -*- coding: utf-8 -*-
## 用format函数实现对齐打印
s='ABC{},\n{}创造城市.'
x=s.format('Python',"js")  ### format 依次对应添加进入{}中
print(x)
print()

### 居中对齐 {:^}；靠左对齐 {:<}；靠右对齐 {:>}
print('{} {}'.format('hello','world'),'默认左对齐,不带字段')  # 默认左对齐,不带字段

print('{:^} {:^}'.format('hello','world'),'同上,不带字段') # 同上,不带字段
print('{0} {1}'.format('hello','world'),'带数字编号')  # 带数字编号
print('{0} {1} {0}'.format('hello','world'),'带数字编号,乱序')  # 带数字编号,乱序

print('{:^10} {:>20}'.format('hello','world'),'第一个右对齐10位，第二个右对齐20位') #
print('{:^6}{:^12}'.format("ID","名字"))
print('{:^6}{:^12}'.format("ID","name"))
print('{:^6}{:^12}'.format("hellow","world"))
print("{0:^10} {1:^20} {1:10}".format("age","name")) ## 编号加占位符（输出宽度约束为20个字符）
print("{0:a<10}".format("age"))
print()

### 中文字符在字符占用上相当于两个英文字符，但是字体设计上，一般一个中文字符的宽度不会等于两个英文字符的宽度，所以打印出来的效果有偏差。
print('{:<10}{:>20}'.format('hello','world'))
## 字符原长度不够10或者20，则会填充$或者*。
print('{:$<10}++{:*>20}'.format('hello','world')) ## $个数+字母个数=10；*个数+字母个数=20
print('{:$<10}++{:*>20}'.format('汉','字'))  ## $个数+汉字个数=10；*个数+汉字个数=20
print('{:$^10}++{:*^20}'.format('hello','world'))
print('{:$^10}++{:*^20}'.format('汉','字'))
a='hello'.encode('gbk')
b='汉'.encode('gbk')
print(a, b, '汉字和字母gbk格式的长度差：', len(b)-len(a))
print('汉字字节长度与汉字gbk格式长度差：%d'%(len('hello')-len(a)))
print()

## 英文或者符号输出
def show(n):
    tail = "*"*(2*n-1)   #最底下一行显示出（2*n-1)个星号
    width = len(tail)   #计算星号所在行的宽度，作为其他行的对齐基准
    for i in range(1,2*n,2):
        print("{:^{}}".format("*"*i,width))
show(5)

def show(n):
    tail = "好"*(2*n-1)   #最底下一行显示出（2*n-1)个星号
    width = len(tail)   #计算星号所在行的宽度，作为其他行的对齐基准
    for i in range(1,2*n,2):
        print("{:^{}}".format("好"*i,width))
show(5)

#######  中文字符在字符占用上相当于两个英文字符，但是字体设计上，一般一个中文字符的宽度不会等于两个英文字符的宽度，所以打印出来的效果有偏差。

format_title='{:^6}{:^12}\t{:^8}\t{:^10}\t{:^10}'
print(format_title.format("ID","名字","英语成绩","Python成绩","C语言成绩","总成绩"))
print()


c = [
    '决',
    '决决',
    '决决决',
    '决决决决',
    '决决决决决',
    '决决决决决决',
    '决决决决决决决'
]
print('----正常字符串格式化：----')
for x in range(len(c)):
    print('|%20s|' % c[x])
print('============')
c = [
    '决',
    '决决',
    '决决决',
    '决决决决',
    '决决决决决',
    '决决决决决决',
    '决决决决决决决'
]
print('----正常字符串格式化：----')
for x in range(len(c)):
	print(c[x])
print()

###
### 如%10d，%10s,%10f ,指定输出宽度为10，不足则左侧补空格，也就是右对齐
### 如%-10d，%-10s,%-10f ,指定输出宽度为10，不足则右侧补空格，也就是左对齐
### \t表示的是制表符，能有很好的实现列对齐.对齐的规则是，在\t之前的内容的大小为n，若n不是8的倍数，对其在右侧空格补齐为8的倍数，如果大小正好是8的倍数，则右侧再补8个空格。
print("%-8s\t%-8s\t%-8s\t%-8s"%("Name", "Chinese", "Math", "English"))
print("%-10s\t%-10d\t%-10d\t%-10d\t"%("LiMing",99, 100, 100))
print("%-10s\t%-10d\t%-10d\t%-10d\t"%("SunHong",90, 88, 96))
print("%-10s\t%-10d\t%-10d\t%-10d\t"%("WangJing",99, 95, 98))
print('**'*20)

str1 = '陈丽丽'
str2 = 'a'
str3 = 'abcd'
print(str1.encode('gbk'), '\n',  # b'\xb3\xc2\xc0\xf6\xc0\xf6'
	  str2.encode('gbk'), '\n',  # b'a'
	  str3.encode('gbk'))  # b'abcd'

print(len(str1.encode('gbk')))  # 6
print(len(str2.encode('gbk')))  # 1
print(len(str3.encode('gbk')))  # 4
### \x表示16进制 ，\xb3表示一个字节,所以“陈丽丽”三个字6个字节.'a','abcd'分别一和四个字节
print('&&'*20)

def align(str1, distance, alignment='left'):
	length = len(str1.encode('gbk'))
	space_to_fill = distance - length if distance > length else 0
	if alignment == 'left':
		str1 = str1 + ' ' * space_to_fill
	elif alignment == 'right':
		str1 = ' ' * space_to_fill + str1
	elif alignment == 'center':
		str1 = ' ' * (distance // 2) + str1 + ' ' * (distance - distance // 2)
	return str1


print(align('姓名', 20), align('电话', 20), align('QQ', 20), align('邮箱', 20))

print(align('cxj', 20), align('17854264217', 20),
	  align('1239112948', 20), align('1239112948@qq.com', 20))

print(align('陈丽丽', 20), align('17854264217', 20),
	  align('1239112948', 20), align('1239112948@qq.com', 20))
print()

###
name='痛苦之影'
x='c5:12.454 steam:18.353'
print('[{name:<{len}}\t%s'.format(name=name+']',len=22-len(name.encode('GBK'))+len(name))%x)
print()

######  print()
x=100
print('x=/%6d/'%x)
y=10.5
print('y=/%6.3f/'%y)