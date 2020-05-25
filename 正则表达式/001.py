# 生活不会突变，你要做的只是耐心和积累。人这一辈子没法做太多的事情，所以每一件尽力而为。
# -*- coding: utf-8 -*-

import re

sentence = 'This is a sample string'
words = ['cat', 'attempt', 'tattle']
pet_sentence1 = 'They bought a dog'
pet_sentence2 = 'A cat crossed their path'
byte_data = b'This is a sample string'

# bool() 函数用于将给定参数转换为布尔类型，如果没有参数，返回 False。
print(bool(re.search(r'is',sentence)))


# all() 函数用于判断给定的可迭代参数 iterable 中的所有元素是否都为 TRUE，
# 如果是返回 True，否则返回 False。
# 元素除了是 0、空、None、False 外都算 True
print(all(re.search(r'at', w) for w in words))


# any() 函数用于判断给定的可迭代参数 iterable 是否全部为 False，则返回 False，
# 如果有一个为 True，则返回 True。
# 元素除了是 0、空、FALSE 外都算 TRUE。
print(any(re.search(r'stat', w) for w in words))


pet = re.compile(r'dog')
# print(type(pet))  # 返回 <class 're.Pattern'>
print(pet.search(pet_sentence1))
print(re.compile(r'dog').search(pet_sentence1))
print(pet.search(pet_sentence2))
print('================')

word = re.compile(r'is')
# search for 'is' starting from 5th character of 'sentence' variable [0,1,2,3,4]
print(word.search(sentence, 4))  ## 从第4个字符串后开始

print(word.search(sentence, 6))
print(word.search(sentence[6:]))   ## 同上，字符串切片

print(word.search(sentence, 2, 4))  # 空格是不算数的

print(word.search(sentence[2:4]))   # 字符串切片


## 如果你的系统是windows的话，请将 \n替换成\r\n
## 记忆方式：A-Z（字母表）  \A:字符串开始
##
print(re.search(r'\Acat', 'cater'))  # 作为前缀用法\A, cater 从第一个起'cat'

print(re.search(r'\Acat', 'concatenation'),'\n')  # 作为前缀用法\A, concatenation 从第一个起'con' 不是 'cat'


# 默认地，字符串数据默认是"单独"的一句
print(re.search(r'\Ahi', 'hi hello\ntop spot'))

# 返回 False 说明\n的句子不算开头
print(re.search(r'\Atop', 'hi hello\ntop spot'))

# 记忆方式：A-Z（字母表）
# \Z:字符串结尾
print(bool(re.search(r'are\Z', 'spare')))  # 注意和\A 的区别

print(bool(re.search(r'are\Z', 'nearest')))


words = ['surrender', 'unicorn', 'newer', 'door', 'empty', 'eel', 'pest']
# for w in words:
#   if re.search(r'er\Z', w):
#        print(w)
print([w for w in words if re.search(r'er\Z', w)])  # 以er结尾的
# 返回 ['surrender', 'newer']
print([w for w in words if re.search(r't\Z', w)])  # 以t结尾的
# 返回 ['pest']


word_pat = re.compile(r'\Acat\Z')  # 和 == 的作用是相同的  匹配 cat 字符串
print(bool(word_pat.search('cat')))
# 返回 True
print(bool(word_pat.search('cater')))
# 返回 False
print(bool(word_pat.search('concatenation')))
# 返回 False


print(re.sub(r'\A', r're', 'live'))  # \A默认第一个字母
# 返回 'relive'
print(re.sub(r'\A', r're', 'send'))
# 返回 'resend'
print(re.sub(r'\Z', r'er', 'cat'))
# 返回 'cater'
print(re.sub(r'\Z', r'er', 'hack'))
# 返回 'hacker'

a = re.sub(r"hello", "i love the", "hello world")
print(a)            ## i love the world

# 由于strings值是不可改变的，所以无法改变初始值。
word = 'cater'
print(re.sub(r'\Acat', r'hack', word))
# 返回 'hacker'
print(word)
# 返回 'cater'

# need to explicitly assign the result if 'word' has to be changed
# 需要将值重新赋予给 'word'
word = re.sub(r'\Acat', r'hack', word)
print(word)

pets = 'cat and dog'
# ^ 类似于\A 的作用
print(bool(re.search(r'^cat', pets)))
# 返回 True
print(bool(re.search(r'^dog', pets)))
# 返回 False

# $ 类似于\Z 的作用
print(bool(re.search(r'dog$', pets)))
# 返回 True
print(bool(re.search(r'^dog$', pets)))
# 返回 False


# $ 可以匹配字符串的末尾数据，和最后一个换行字符之前的数据。区别于\Z。
greeting = 'hi there\nhave a nice day\n'
print(bool(re.search(r'day$', greeting)))  # 返回 True
print(re.sub(r'day$', "", greeting))
# 返回 have a nice \n
print(bool(re.search(r'day\n$', greeting)))  # 返回 True
print(re.sub(r'day\n$', "", greeting))
# 返回 have a nice

print(bool(re.search(r'day\Z', greeting)))  # 返回 False
# 原因是匹配不到day
print(bool(re.search(r'day\n\Z', greeting)))  # 返回 True
print(re.sub(r'day\n\Z', "", greeting))
# 返回 have a nice

print('========== 多行匹配 =========')

####   多行(multiple line)实现规则
# 返回 True 对每行进行查询，是否存在^是top (存在第二行)
print(re.search(r'^top', 'hi hello\ntop spot', flags=re.M))

print(re.search(r'ar$', 'spare\npar\ndare', flags=re.M))

elements = ['spare\ntool', 'par\n', 'dare']
print([e for e in elements if re.search(r'are$', e, re.M)])  # 运用遍历的方式把符合$是are的取出来
# 返回 ['spare\ntool', 'dare']


ip_lines = 'catapults\nconcatenate\ncat'
print(re.sub(r'^', r'* ', ip_lines, flags=re.M))  # 和\A 的区别在于没有直接将"第一个字母"替换掉。
# 返回
#       * catapults
#       * concatenate
#       * cat

print(re.sub(r'\A', r'* ', ip_lines, flags=re.M))
#       * catapults
#       concatenate
#       cat

print(re.sub(r'$', r'.', ip_lines, flags=re.M))
# 返回
#       catapults.
#       concatenate.
#       cat.


###  \b 定义为：界定符
words = 'par spar apparent spare part'
# 对所有的'对象'进行替换
print(re.sub(r'par', r'X', words))
# 返回 'X sX apXent sXe Xt'

# 注意\b, 对开头是'对象'的单位进行替换
print(re.sub(r'\bpar', r'X', words))
# 返回 'X spar apparent spare Xt'

# 注意\b, 对结尾是'对象'的单位进行替换
print(re.sub(r'par\b', r'X', words))
# 返回 'X sX apparent spare part'

# 注意\b, 两个\b效果相等于 ==
print(re.sub(r'\bpar\b', r'X', words))
# 返回 'X spar apparent spare part'



words = 'par spar apparent spare part'
print(re.sub(r'\b', r'"', words).replace(' ', ','))
'''
words = \bpar\b\bspar\b\bapparent\b\bspare\b\bpart\b
# 第一步，将每个\b用""替代；
# 第二步，将每个' '用','替代
'''
# 返回 "par","spar","apparent","spare","part"

print(re.sub(r'\b', r' ', '-----hello-----'))
# 返回 '----- hello -----'
'''
Word anchors: Alphabets (irrespective of case), digits and the underscore character, but the dash is not included
单词锚：字母（不区分大小写），数字和下划线，但不包括破折号
所以：-----\bhello\b-----
'''
# make a programming statement more readable
# shown for illustration purpose only, won't work for all cases
print(re.sub(r'\b', r' ', 'foo_baz=num1+35*42/num2'))
# 返回 ' foo_baz = num1 + 35 * 42 / num2 '
'''\bfoo_baz\b=\bnum1\b+\b35\b*\b42\b/\bnum2\b'''

# excess space at start/end of string can be stripped off 句首/句末的多余space可被剥离掉
# later you'll learn how to add a qualifier so that strip is not needed
print(re.sub(r'\b', r' ', 'foo_baz=num1+35*42/num2').strip())
# 返回 'foo_baz = num1 + 35 * 42 / num2'



'''
	\b，\B是单词边界，不匹配任何实际字符，所以是看不到的；\B是\b的非(补)。

	\b：表示字母数字与非字母数字的边界，非字母数字与字母数字的边界。
	
	\B：表示字母数字与(非非)字母数字的边界，非字母数字与非字母数字的边界。
'''

words = 'par spar apparent spare part'
'''
\bpar\b \bspar\b \bapparent\b \bspare\b \bpart\b
'''
# replace 'par' if it is not start of word
print(re.sub(r'\Bpar', r'X', words))  # \Bpar = par\b 或者 par
# 返回 'par sX apXent sXe part'
'''
print(re.sub(r'\bpar', r'X', words))
# 返回 'X spar apparent spare Xt'

'''
print(re.sub(r'\Bpar\b', r'X', words))  # \Bpar\b = par\b
# 返回 'par sX apparent spare part'
'''
print(re.sub(r'\bpar', r'X', words))
# 返回 'X spar apparent spare Xt'
'''
print(re.sub(r'par\B', r'X', words))  # par\B = \bpar = par
# 返回 'par spar apXent sXe Xt'
'''
print(re.sub(r'par\b', r'X', words))
# 返回 'X sX apparent spare part'
'''
print(re.sub(r'\Bpar\B', r'X', words))  # \Bpar\B = par
# 返回 'par spar apXent sXe part'
'''
print(re.sub(r'\bpar\b', r'X', words))
# 返回 'X spar apparent spare part'
'''
# Here's some standalone pattern usage to compare and contrast the two word anchors.
# 下面是一些独立的用法，来对比一下这两个单词锚。
print(re.sub(r'\b', r':', 'copper'))  # \bcopper\b = c\Bo\Bp\Bp\Be\Br
# 返回 ':copper:'
print(re.sub(r'\B', r':', 'copper'))  # \bcopper\b = c\Bo\Bp\Bp\Be\Br
# 返回 'c:o:p:p:e:r'

print(re.sub(r'\b', r' ', '-----hello-----'))  # -----\bhello\b-----
# 返回 '----- hello -----'
print(re.sub(r'\B', r' ', '-----hello-----'))  # \B-\B-\B-\B-\B-h\Be\Bl\Bl\Bo-\B-\B-\B-\B-\B
# 返回 ' - - - - -h e l l o- - - - - '


import re
words = ['hi42bye', 'nice1423', 'bad42', 'cool_42a', 'fake4b']
print([w for w in words if re.search(r'42\B', w)])
## 输出结果：['hi42bye', 'nice1423', 'cool_42a']


import re
foo = ['lovely', '1 dentist', '2 lonely', 'eden', 'fly away', 'dent']
print([e for e in foo if re.search(r'^den', e) or re.search(r'ly$', e)])
### 输出结果：['lovely', '2 lonely', 'dent']


import re
para = '''\
ball fall wall tall
mall call ball pall
wall mall ball fall'''
print(re.sub(r'^mall', r'1234', para, flags=re.M))
'''
	输出结果：
	ball fall wall tall
	1234 call ball pall
	wall mall ball fall
'''