# 生活不会突变，你要做的只是耐心和积累。人这一辈子没法做太多的事情，所以每一件尽力而为。
# -*- coding: utf-8 -*-

import re

# ab*c = ac \ abc \ abbc \ abbbc \ ... 不过只匹配一次即abc, 懒惰模式
print(re.search(r'ab*c', 'abc ac adc abbbc'))
# 返回 <re.Match object; span=(0, 3), match='abc'>

# b.*d = bd \ b.d \ b..d \ ... 不过只匹配一次即bc ac ad
print(re.search(r'b.*d', 'abc ac adc abbbc'))
# 返回 <re.Match object; span=(1, 9), match='bc ac ad'>


print(re.search(r'b.*d', 'abc ac adc abbbc'))
# 返回 <re.Match object; span=(1, 9), match='bc ac ad'>

# retrieving entire matched portion
print(re.search(r'b.*d', 'abc ac adc abbbc')[0])  # 用[0]可以返回到具体的值bc ac ad
# 返回 'bc ac ad'

# can also pass an index by calling 'group' method on the Match object
print(re.search(r'b.*d', 'abc ac adc abbbc').group(0))  # [0] == .group[0]
# 返回 'bc ac ad'

# a(.*)d(.*a): 第一个(.*)对应[1]第二个(.*)对应[2] 具体看下面的print
m = re.search(r'a(.*)d(.*a)', 'abc ac adc abbbc')
print(m[1])
# 返回 bc ac a

print(m[2])
# 返回 'c a'

print(m[0])  ## 贪婪模式
# abc ac adc a

# to get a tuple of all the capture groups  # 得到一个元组，即上方的m[1] m[2]
print(m.groups())
# 返回 ('bc ac a', 'c a')

print(re.sub(r'(a|b)\^2', lambda m: m[0].upper(), 'a^2 + b^2 - C*3'))
# (a|b)\^2 : \^ 实际效果：^
# 返回 'A^2 + B^2 - C*3'
# lambda m: m[0].upper() : 设上述(a|b)\^2 = m 则 m[0] = a|b 然后用upper 大写

print('======== re.findall ==========')
# findall 返回的数据是list
print(re.findall(r'ab*c', 'abc ac adc abbbc'))  # ab*c = ac \ abc \ abbc \ ...
# 返回 ['abc', 'ac', 'abbbc']

print(re.findall(r'ab+c', 'abc ac adc abbbc'))  # ab+c = abc \ abbc \ ...
# 返回 ['abc', 'abbbc']

# \bs?pare?\b = \b(s|)par(e|)\b = spar \ spare \ par \ pare
print(re.findall(r'\bs?pare?\b', 'par spar apparent spare part pare'))
# 返回 ['par', 'spar', 'spare', 'pare']

# t.*a = ta \ t.a \ t..a \ ... greedy metacharacter
print(re.findall(r't.*a', 'that is quite a fabricated tale'))
# 返回 ['that is quite a fabricated ta']

print(re.findall(r't.*?a', 'that is quite a fabricated tale'))  # t.*?a = ta \ t.a \ t..a \ ... non-greedy metacharacter
# 返回 ['tha', 't is quite a', 'ted ta']


print(re.findall(r'a(b*)c', 'abc ac adc abbc xabbbcz bbb bc abbbbbc'))
# 返回 ['b', '', 'bb', 'bbb', 'bbbbb']
# a(b*)c = a()c \ a(b)c ...  注意这里的()，在findall函数中实际返回的就是()中的内容

print(re.findall(r'(x*):(y*)', 'xx:yyy x: x:yy :y'))
# 返回 [('xx', 'yyy'), ('x', ''), ('x', 'yy'), ('', 'y')]


### re.findall()如果可以匹配返回的是一个列表
### re.finditer()返回的是一个迭代器，需要对其进行遍历，才能获取数据
print(re.findall(r'(x*):(y*)', 'xx:yyy x: x:yy :y :'))
# 返回 [('xx', 'yyy'), ('x', ''), ('x', 'yy'), ('', 'y'), ('', '')]

print(re.finditer(r'ab+c', 'abc ac adc abbbc'))
# 返回 <callable_iterator object at 0x7fb65e103438>
m_iter = re.finditer(r'ab+c', 'abc ac adc abbbc')  # ab+c = abc \ abbc \ ...
for m in m_iter:
	print(m)

# 返回 <re.Match object; span=(0, 3), match='abc'>
# 返回 <re.Match object; span=(11, 16), match='abbbc'>

# same as: re.findall(r'(x*):(y*)', 'xx:yyy x: x:yy :y')
m_iter = re.finditer(r'(x*):(y*)', 'xx:yyy x: x:yy :y')
print([(m[1], m[2]) for m in m_iter])
# 返回 [('xx', 'yyy'), ('x', ''), ('x', 'yy'), ('', 'y')]

'''Here's some more examples.'''
# work with entire matched portions
m_iter = re.finditer(r'ab+c', 'abc ac adc abbbc')
for m in m_iter:
	print(m[0].upper())

# 返回 ABC
# 返回 ABBBC

# to get start and end+1 index of entire matched portion
# pass a number as argument to get span of that particular capture group
m_iter = re.finditer(r'ab+c', 'abc ac adc abbbc')
for m in m_iter:
	print(m.span())

# 返回 (0, 3)
# 返回 (11, 16)