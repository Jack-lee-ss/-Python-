# 生活不会突变，你要做的只是耐心和积累。人这一辈子没法做太多的事情，所以每一件尽力而为。
# -*- coding: utf-8 -*-

import re

str1 = 'def factorial()'
str2 = 'a/b(division) + c%d(#modulo) - (e+(j/k-3)*4)'
str3 = 'Hi there(greeting). Nice day(a(b)'

remove_parentheses_1 = re.compile(r'\(\)')  ##### add your solution here
print(remove_parentheses_1.sub('', str1))
print(re.search('.*l', str1).group())
print(re.findall('(.*?)\(', str1)[0])
print(re.sub('\(\)', '', str1))
# 返回 'def factorial'

remove_parentheses_2 = re.compile(r'\(....\w*?\)')
print(remove_parentheses_2.sub('', str2))
print(re.sub('\(....\w*?\)', '', str2))
# 返回 'a/b + c%d - (e+*4)'

remove_parentheses_3 = re.compile(r'\(\w*?\)')
print(remove_parentheses_3.sub('', str3))
print(re.sub('\(\w*?\)', '', str3))
# 返回 'Hi there. Nice day(a'

str4 = '128A foo 0xfe32 34 0xbar'
hex_seq = re.compile(r'(\d.*?)')  ##### add your solution here
print(re.findall("(\d.*?) ", str4))
# 返回 ['128A', '0xfe32', '34']

str5 = '0XDEADBEEF place 0x0ff1ce bad'
print(re.findall('(0.*? |..d.*?)', str5))

# 返回 ['0XDEADBEEF', '0x0ff1ce', 'bad']

str6 = 'hi0000432abcd'
# print(bool(re.search('aa',str6)))  # 随便一个不匹配的都是False
print(int(re.search(r"\d+", str6).group()) > 624)  # 匹配里面的数字并检测是否大于624，如果小于624则返回False，如果大于则True
# 返回 False

str7 = '42_624 0512'
# print(bool(re.search('aa',str7)))  # 随便一个不匹配的都是False
print(int(re.search(r"\d\d\d+", str7).group()) > 624)  # 匹配里面的数字并检测是否大于624，如果小于624则返回False，如果大于则True
# 返回 False

str8 = '3.14 96 2 foo1234baz'
# print(bool(re.search('3.14',str8)))  # 随便一个匹配的都是True
print(int(re.search(r"\d\d\d+", str8).group()) > 624)  # 匹配里面的数字并检测是否大于624，如果小于624则返回False，如果大于则True
# 返回 True

str9 = 'lion \t Ink32onion Nice'
str10 = '**1\f2\n3star\t7 77\r**'
expr_9 = re.compile('\W+|\d+')  ##### add your solution here
print(expr_9.split(str9))
# # 返回 ['lion', 'Ink', 'onion', 'Nice']

# expr_10 = re.compile('\s+|\d+')  ##### add your solution here
expr_10 = re.compile('1\f2\n3|\t7 77\r')  ##### add your solution here
print(expr_10.split(str10, 2),'\n')
# 返回 ['**', 'star', '**']
print('=============')




###  \w匹配字母或数字或下划线或汉字等，不包括空格。
###  \s匹配任意的空白符，包括空格，制表符(Tab)，换行符，中文全角空格等
###  \W	匹配任意不是字母，数字，下划线，汉字的字符
###  \S 匹配任意不是空白符的字符
###  ?重复零次或一次(前面的字符串)


print('============ 向后引用 ============')
'''
	 使用小括号指定一个子表达式后，匹配这个子表达式的文本,默认情况下，每个分组会自动拥有一个组号，规则是：从左向右，以分组的左括号为标志，第一个出现的分组的组号为1，第二个为2，以此类推。后向引用用于重复搜索前面某个分组匹配的文本。例如，\1代表分组1匹配的文本.
	
	这个\1  \2......  都要和正则表达式集合()一起使用.
	\1表示重复正则第一个圆括号内匹配到的内容；\2表示重复正则第二个圆括号内匹配到的内容.
	
	\b(\w+)\b\s+\1\b可以用来匹配重复的单词，像go go, 或者kitty kitty (单词开始处和结束处之间的多于一个的字母或数字(\b(\w+)\b)，这个单词会被捕获到编号为1的分组中，然后是1个或几个空白符(\s+)，最后是分组1中捕获的内容（也就是前面匹配的那个单词）(\1))
	
	自己指定子表达式的组名:(上述是默认\1指代匹配内容)(?<Word>\w+)(或者把尖括号换成'也行：(?'Word'\w+)),这样就把\w+的组名指定为Word了。要反向引用这个分组捕获的内容，你可以使用\k<Word>。\b(?<Word>\w+)\b\s+\k<Word>\b。
	
	
'''
r=re.compile(r'\b(\w+)\b\s+\1\b')
print(r.match('kitty kitty'))


print(re.sub(r'\[(\d+)\]', r'\1', '[52] apples and [31] mangoes'))
# 返回 '52 apples and 31 mangoes'

print(re.sub(r'(_)?_', r'\1', '_foo_ __123__ _baz_'))
## (_)?_ == ((_)|)_ == (_)_ | _
# 返回 'foo _123_ baz'

'''
	向后引用，给出第N个捕获组的匹配部分,可能的值：\ g <0>，\ g <1>等（不限于99）,\ g <0>指整个匹配部分.
	r'(\g<0>0)': 匹配的文本添加数字0.外加一个（）
	
'''
print(re.sub(r'(\d+)', r'(\g<0>0)', '52 apples and 31 mangoes'))
# 返回 '(520) apples and (310) mangoes'

print(re.sub(r'(\d+)', r'(\g<0>100)', '52 apples and 31 mangoes'))
## (52100) apples and (31100) mangoes

print(re.sub(r'(\d+)',r'(\1+0)','52 apples and 31 mangoes'))
## (52+0) apples and (31+0) mangoes

print(re.sub(r'.*', r'Hi. \g<0>. Have a nice day', 'Hello world', count=1))
# 返回 'Hi. Hello world. Have a nice day'


## 对调两个文本的位置
print(re.sub(r'(\w+),(\w+)', r'\2,\1', 'good,bad 42,24'))
'bad,good 24,42'


words = ['effort', 'flee', 'facade', 'oddball', 'rat', 'tool']
print([w for w in words if re.search(r'\b\w*(\w)\1\w*\b', w)]) ## 匹配含有重复字符的字符串
# 返回 ['effort', 'flee', 'oddball', 'tool']

print(re.sub(r'\b(\w+)( \1)+\b', r'\1', 'aa a a a 42 f_1 f_1 f_13.14'))
# 返回 'aa a 42 f_1 f_13.14'


print(re.split(r'\d+', 'Sample123string42with777numbers'))
# 返回 ['Sample', 'string', 'with', 'numbers']

print(re.findall(r'[^0-9]+','Sample123string42with777numbers'))

print(re.findall(r'\d+','Sample123string42with777numbers'))

print(re.split(r'(\d+)', 'Sample123string42with777numbers'))
# 返回 ['Sample', '123', 'string', '42', 'with', '777', 'numbers']

print(re.split(r'(1*2)', '3111111111125111142', maxsplit=1),'\n')
# 返回 ['3', '11111111112', '5111142']

print('============ (?:exp)	匹配exp,不捕获匹配的文本，也不给此分组分配组号 =============')

## 匹配带有 st|in 结尾的字符串。
print(re.findall(r'\b\w*(?:st|in)\b', 'cost akin more east run against'))
# 返回 ['cost', 'akin', 'east', 'against']


## 分隔符是以 含有一个或者多个 y|ful字符的字符串作为分隔符。
print(re.split(r'hand(?:y|ful)?', '123hand42handy777handful500'))
# 返回 ['123', '42', '777', '500']

### count=1  ： 只处理第一个符合该规则的字符串
print(re.sub(r'\A(([^,]+,){3})([^,]+)', r'\1(\3)', '1,2,3,4,5,6,7', count=1))
# 返回 '1,2,3,(4),5,6,7'


print(re.sub(r'\A((?:[^,]+,){3})([^,]+)', r'\1(\2)', '1,2,3,4,5,6,7', count=1))
# 返回 '1,2,3,(4),5,6,7'


words = 'effort flee facade oddball rat tool'

repeat_char = re.compile(r'\b\w*(\w)\1\w*\b')   ### 匹配重复字符

print(repeat_char.findall(words))
# 返回 ['f', 'e', 'l', 'o']


m_iter = repeat_char.finditer(words)            ## 找出含有重复字符的字符串
print([m[0] for m in m_iter])
# 返回 ['effort', 'flee', 'oddball', 'tool']


print(re.sub(r'(?P<fw>\w+),(?P<sw>\w+)', r'\g<sw>,\g<fw>', 'good,bad 42,24')) ## 对调字符串
# 返回 'bad,good 24,42'

sentence = 'I bought an apple'
m = re.search(r'(?P<fruit>\w+)\Z', sentence)
print(m[1])
# 返回 'apple'

print(m['fruit'])
# 返回 'apple'

print(m.group('fruit'))
# 返回 'apple'


import re, regex

row = 'today,2008-03-24,food,2012-08-12,nice,5632'

print(re.search(r'\d{4}-\d{2}-\d{2}.*\d{4}-\d{2}-\d{2}', row)[0])
# 返回 '2008-03-24,food,2012-08-12'

print(regex.search(r'(\d{4}-\d{2}-\d{2}).*(?1)', row)[0])
# 返回 '2008-03-24,food,2012-08-12'


import regex

row = 'today,2008-03-24,food,2012-08-12,nice,5632'

print(regex.search(r'(?P<date>\d{4}-\d{2}-\d{2}).*(?&date)', row)[0])
# 返回 '2008-03-24,food,2012-08-12'


'''
	零宽断言:
	零宽度正预测先行断言 : 用于查找在某些内容(但并不包括这些内容)之前或之后的东西,(?=exp)也叫零宽度正预测先行断言，它断言自身出现的位置的后面能匹配表达式exp. (?=exp) 标志位前面内容
	
	零宽度正回顾后发断言: 它断言自身出现的位置的前面能匹配表达式exp,  (?<=exp) 标志位后面内容
'''
## 匹配以ing结尾的单词的前面部分(除了ing以外的部分)
r=re.compile(r'\b\w+(?=ing\b)')
print(r.findall('I m singing while you re dancing'))  #  ['sing', 'danc']


r=re.compile(r'(?<=\d{2})\d+\b')
print(r.findall('1234567890'))       # ['34567890']


r=re.compile(r'(?<=\s)\d+(?=\s)')    ## 匹配以空白符间隔的数字(再次强调，不包括这些空白符)。
print(r.findall('3423 4355 53ghf 45346 435346'))   # ['4355', '45346']


'''
	负向零宽断言:只匹配一个位置，并不消费任何字符
		零宽度负预测先行断言：(?!exp) 断言此位置的后面不能匹配表达式exp
			\d{3}(?!\d)匹配三位数字，而且这三位数字的后面不能是数字
			\b((?!abc)\w)+\b匹配不包含连续字符串abc的单词
		
		零宽度负回顾后发断言：(?<!exp) 断言此位置的前面不能匹配表达式exp
			(?<![a-z])\d{7} 匹配前面不是小写字母的七位数字。
			(?<=<(\w+)>).*(?=<\/\1>) 匹配不包含属性的简单HTML标签内里的内容((?<=<(\w+)>)指定了这样的前缀：被尖括号括起来的单词(比如可能是<b>)，然后是.*(任意的字符串),最后是一个后缀(?=<\/\1>)。注意后缀里的\/，它用到了前面提过的字符转义；\1则是一个反向引用，引用的正是捕获的第一组，前面的(\w+)匹配的内容，这样如果前缀实际上是<b>的话，后缀就是</b>了。整个表达式匹配的是<b>和</b>之间的内容(再次提醒，不包括前缀和后缀本身))
		
'''

r=re.compile(r'\d{3}(?!\d)')
print(r.findall('343ghj g7848hgd'))   ## ['343', '848']

r=re.compile(r'\b((?!abc)\w)+\b')
print(r.findall('abcgh ghabc45 56abdf'))

r=re.compile(r'(?<![a-z])\d{7}')          # ['f']
print(r.findall('ASDFGHJ45434567gfh'))   ## ['4543456']


print('++++++++++++++++++')

print(re.sub(r'foo(?!\d)', r'baz', 'hey food! foo42 foot5 foofoo'))
# 返回 'hey bazd! foo42 bazt5 bazbaz'

print(re.compile(r'foo(?!\d)').findall('hey food! foo42 foot5 foofoo'))
## ['foo', 'foo', 'foo', 'foo']

print(re.sub(r'(?<!_)foo', r'baz', 'foo _foo 42foofoo')) ## 匹配 foo 前面不能有_ 的字符串。
# 返回 'baz _foo 42bazbaz'

print(re.sub(r'(?<!_)foo.', r'baz', 'food _fool 42foo_foot'))
# 返回 'baz _fool 42bazfoot'


print(re.sub(r'(?<![:-])\b\w+\b', r'X', ':cart <apple -rest ;tea'))
# 返回 ':cart <X -rest ;X'

print(re.escape(r'foo_baz=num1+35*42/num2'))
print(re.sub(r'(?<!\A)\b(?!\Z)', r' ', 'foo_baz=num1+35*42/num2'))
# 返回 'foo_baz = num1 + 35 * 42 / num2'


print(re.findall(r'\d+(?=,)', '42 foo-5, baz3; x-83, y-20: f12'))
# 返回 ['5', '83']

print(re.findall(r'(?<=-)\d+(?=[:;])', '42 foo-5, baz3; x-83, y-20: f12'))
# 返回 ['20']

print(re.findall(r'(?<=,)[^,]+(?=,)', '1,two,3,four,5'))  ##
# 返回 ['two', '3', 'four']


print(re.findall(r'(?<=;)[^;]+(?=,)', '1;two,3,4 ,four,5'))
## ['two,3,4 ,four']

print(re.sub(r'(?<![^,])(?![^,])', r'NA', ',1,,,two,3,,,'))
# 返回 'NA,1,NA,NA,two,3,NA,NA,NA'

print(re.sub(r'(\S+\s+)(?=(\S+)\s)', r'\1\2\n', 'a b c d e'))
# 返回
#   a b
#   b c
#   c d
#   d e


print(re.findall(r'(?<=(po|ca)re)\d+', 'pore42 car3 pare7 care5'))
# 返回 ['po', 'ca']
print(re.findall(r'(?<=(?:po|ca)re)\d+', 'pore42 car3 pare7 care5'))
# 返回 ['42', '5']

words = ['sequoia', 'subtle', 'questionable', 'exhibit', 'equation']

# same as: r'b.*e.*t|b.*t.*e|e.*b.*t|e.*t.*b|t.*b.*e|t.*e.*b'
print([w for w in words if re.search(r'(?=.*b)(?=.*e).*t', w)])
# 返回 ['subtle', 'questionable', 'exhibit']


print([w for w in words if re.search(r'(?=.*a)(?=.*e)(?=.*i)(?=.*o).*u', w)])
# 返回 ['sequoia', 'questionable', 'equation']


print(re.findall(r'(?<=(?:po|ca)re)\d+', 'pore42 car3 pare7 care5'))
# 返回 ['42', '5']
print(re.findall(r'(?<=\b[a-z]{4})\d+', 'pore42 car3 pare7 care5'))
# 返回 ['42', '7', '5']

# not allowed
print(re.findall(r'(?<!car|pare)\d+', 'pore42 car3 pare7 care5'))
# 返回 re.error: look-behind requires fixed-width pattern
print(re.findall(r'(?<=\b[a-z]+)\d+', 'pore42 car3 pare7 care5'))
# 返回 re.error: look-behind requires fixed-width pattern
print(re.sub(r'(?<=\A|,)(?=,|\Z)', r'NA', ',1,,,two,3,,,'))
# 返回 re.error: look-behind requires fixed-width pattern


import regex

# similar to: r'(?<=\b\w)\w*\W*'
# text matched before \K won't be replaced
print(regex.sub(r'\b\w\K\w*\W*', r'', 'sea eat car rat eel tea'))
# 返回 'secret'

# replace only 3rd occurrence of 'cat'
print(regex.sub(r'(cat.*?){2}\Kcat', r'X', 'cat scatter cater scat', count=1))
# 返回 'cat scatter Xer scat'

'''The regex module allows using variable length lookbehind without needing any change.'''
print(regex.findall(r'(?<=\b[a-z]+)\d+', 'pore42 car3 pare7 care5'))
# 返回 ['42', '3', '7', '5']

print(regex.sub(r'(?<=\A|,)(?=,|\Z)', r'NA', ',1,,,two,3,,,'))
# 返回 'NA,1,NA,NA,two,3,NA,NA,NA'

print(regex.sub(r'(?<=(cat.*?){2})cat', r'X', 'cat scatter cater scat', count=1))
# 返回 'cat scatter Xer scat'

'''Here's some variable length negative lookbehind examples.'''
print(regex.findall(r'(?<!car|pare)\d+', 'pore42 car3 pare7 care5'))
# 返回 ['42', '5']

# match 'dog' only if it is not preceded by 'cat'
print(bool(regex.search(r'(?<!cat.*)dog', 'fox,cat,dog,parrot')))
# 返回 False

# match 'dog' only if it is not preceded by 'parrot'
print(bool(regex.search(r'(?<!parrot.*)dog', 'fox,cat,dog,parrot')))
# 返回 True

'''Negated groups
This will work for both re and regex modules. This also showcases how grouping can be negated in certain cases.
'''
# note the use of \A anchor to force matching all characters up to 'dog'
print(bool(re.search(r'\A((?!cat).)*dog', 'fox,cat,dog,parrot')))
# 返回 False
print(bool(re.search(r'\A((?!parrot).)*dog', 'fox,cat,dog,parrot')))
# 返回 True

# easier to understand by checking matched portion
print(re.search(r'\A((?!cat).)*', 'fox,cat,dog,parrot')[0])
# 返回 'fox,'
print(re.search(r'\A((?!parrot).)*', 'fox,cat,dog,parrot')[0])
# 返回 'fox,cat,dog,'
print(re.search(r'\A((?!(.)\2).)*', 'fox,cat,dog,parrot')[0])
# 返回 'fox,cat,dog,pa'

'''As lookarounds do not consume characters, don't use variable length lookbehind between two patterns (assuming regex module).
Use negated groups instead.
'''
# match if 'do' is not there between 'at' and 'par'
print(bool(re.search(r'at((?!do).)*par', 'fox,cat,dog,parrot')))
# 返回 False

# match if 'go' is not there between 'at' and 'par'
print(bool(re.search(r'at((?!go).)*par', 'fox,cat,dog,parrot')))
# 返回 True
print(re.search(r'at((?!go).)*par', 'fox,cat,dog,parrot')[0])
# 返回 'at,dog,par'

# use non-capturing group if required
print(re.findall(r'a(?:(?!\d).)*z', 'at,baz,a2z,bad-zoo'))
# 返回 ['at,baz', 'ad-z']