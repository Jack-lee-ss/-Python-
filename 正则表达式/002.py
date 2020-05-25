# 生活不会突变，你要做的只是耐心和积累。人这一辈子没法做太多的事情，所以每一件尽力而为。
# -*- coding: utf-8 -*-


import re
'''
	用escape 函数 可以展示出re语言下的具体代码
	
	|”符号的作用 ： 类似于OR，
	

	“|”符号的用法 ：类似于乘法分配律：a(b|c)d = abd|acd
	注意：
	
	alt = re.compile(r'\b(' + '|'.join(words) + r')\b')
	alt.pattern == r'\b(cat|par)\b' = r'\bcat\b|\bpar\b'
	
	Count optional argument here restricts no. of replacements to 1
	print(re.sub(r'year|years', r'X', mood, count=1))
	# 返回 'best Xs'
	print(re.sub(r'years|year', r'X', mood, count=1))
	# 返回 'best X'
	
	alt = re.compile('|'.join(sorted(words, key=len, reverse=True)))
	print(alt.pattern)
	# 返回 'handful|handy|hand'  # 通过长度len进行sort, 然后再进行reverse，从而longest first
	
'''
print('=========== | ============')
# match either 'cat' or 'dog'
print(bool(re.search(r'cat|dog', 'I like cats')))  # 作用和 OR 的作用类似
# 返回 True
print(bool(re.search(r'cat|dog', 'I like dogs')))
# 返回 True
print(bool(re.search(r'cat|dog', 'I like parrots')))
# 返回 False

# replace either 'cat' at start of string or 'cat' at end of word
print(re.sub(r'\Acat|cat\b', r'X', 'catapults concatenate cat scat'))  # \A = ^
# 返回 'Xapults concatenate X sX'

# replace either 'cat' or 'dog' or 'fox' with 'mammal'
print(re.sub(r'cat|dog|fox', r'mammal', 'cat dog bee parrot fox'))
# 返回 'mammal mammal bee parrot mammal'


print('|'.join(['car', 'jeep']))
# 返回 'car|jeep'
words = ['cat', 'dog', 'fox']
print('|'.join(words))
# 返回 'cat|dog|fox'
print(re.sub('|'.join(words), r'mammal', 'cat dog bee parrot fox'))
# 返回 'mammal mammal bee parrot mammal'


# without grouping
print(re.sub(r'reform|rest', r'X', 'red reform read arrest'))
## red X read arX

# with grouping
print(re.sub(r're(form|st)', r'X', 'red reform read arrest'))  # 类似地满足"乘法分配律"
# 返回 'red X read arX'

# without grouping
print(re.sub(r'\bpar\b|\bpart\b', r'X', 'par spare part party'))
# 返回 'X spare X party'

# taking out common anchors
print(re.sub(r'\b(par|part)\b', r'X', 'par spare part party'))
# 返回 'X spare X party'

# taking out common characters as well
print(re.sub(r'\bpar(|t)\b', r'X', 'par spare part party'))
# 返回 'X spare X party'


'''
	pattern == re.compile(...)
'''
words = ['cat', 'par']
alt = re.compile(r'\b(' + '|'.join(words) + r')\b')  # r'\b(cat|par)\b'
# only whole words will be replaced now # 只有完整地一个单词才会被替换
print(alt.sub(r'X', 'cater cat concatenate par spare'))
# 返回 'cater X concatenate X spare'

# this is how the above RE looks as a normal string  将上述的alt的值返回
print(alt.pattern)
# 返回 '\\b(cat|par)\\b'
print(alt.pattern == r'\b(cat|par)\b')  # = r'\bcat\b|\bpar\b'
# 返回 True


words = 'lion elephant are rope not'
## 替换 前几个 符合条件的字符串
print(re.sub(r'on|ant', r'X', words, count=1))  ## 替换第一个
# 返回 'liX elephant are rope not'
print(re.sub(r'ant|on', r'X', words, count=2))  ## 替换前两个
# 返回 'liX elephX are rope not'
print(re.sub(r'years|year', r'X', 'best years', count=1))  # 如果识别重复的话，可以通过顺序来选择替换
## best X



words = 'ear xerox at mare part learn eye'

print(re.sub(r'ar|are|art', r'X', words))  # 没有count 的约束的话，优先第一个开始
# 返回 'eX xerox at mXe pXt leXn eye'

print(re.sub(r'are|ar|art', r'X', words,count=1)) ## 替换前一个符合条件字符串
#      eX xerox at mare part learn eye

# this is going to be same as: r'are|ar'
print(re.sub(r'are|ar|art', r'X', words,count=2)) ## 替换前两个符合条件字符串
# 返回 'eX xerox at mX part learn eye'

# phew, finally this one works as needed
print(re.sub(r'are|art|ar', r'X', words))  # 没有count 的约束的话，按顺序进行替换
# 返回 'eX xerox at mX pX leXn eye'



words = ['hand', 'handy', 'handful']
alt = re.compile('|'.join(sorted(words, key=len, reverse=True)))
print(alt.pattern)
# 返回 'handful|handy|hand'  # 通过长度len进行sort, 然后再进行reverse，从而longest first

print(alt.sub(r'X', 'hands handful handed handy'))
# 返回 'Xs X Xed X'  # 利用'handful|handy|hand' 进行替换

# without sorting, alternation order will come into play
print(re.sub('|'.join(words), r'X', 'hands handful handed handy'))
# 返回 'Xs Xful Xed Xy' # 没有排序的结果

'''
	import re
	foo = ['lovely', '1 dentist', '2 lonely', 'eden', 'fly away', 'dent']
	print([e for e in foo if re.search(r'$ly|^de',e,re.M)])
	['lovely', '2 lonely', 'dent']
	
	
'''

# 用 \ 去匹配一些无法literally匹配到的符号例如下文中的^和(和)
# 用re.escape() 可以看到具体的re识别的代码
# \ 匹配特殊符号 ( ) +  - ^ . 等等

print(re.search(r'b^2', 'a^2 + b^2 - C*3'))  # ^符号是无法字面上匹配到
# 返回 None

print(re.search(r'b\^2', 'a^2 + b^2 - C*3'))  # \^ == ^
# 返回 <_sre.SRE_Match object; span=(6, 9), match='b^2'>


print(re.sub(r'\(|\)', r'', '(a*b) + c'))  # \(|\) == (|) 匹配\( = ( ; \) = )
# 返回 'a*b + c'

print(re.sub(r'\\', r'/', r'\learn\by\example'))  # \\ == \
# 返回 '/learn/by/example'

eqn = 'f*(a^b) - 3*(a^b)'
# straightforward search and replace, no need RE shenanigans
print(eqn.replace('(a^b)', 'c'))  # 也可以直接用search 和 replace函数作业
# 返回 'f*c - 3*c'

expr = '(a^b)'
# print used here to show results similar to raw string
print(re.escape(expr))
# 返回 \(a\^b\)       用escape 函数 可以展示出re语言下的具体代码 1.\(   2.a   3.\^   4.b   5.\)

# replace only at end of string
print(re.sub(re.escape(expr) + r'\Z', r'c', eqn))
# 返回 'f*(a^b) - 3*c'  \(a\^b\)\Z 是指代最后一个\(a\^b\) 即3*(a^b)中的(a^b)， 用c替换
# 这地方的\Z 也可以用$代替

# if strings are to be matched literally,
# need to use re.escape for each string when creating alternations
terms = ['foo_baz', expr]
print('|'.join(re.escape(w) for w in terms))
# 返回 foo_baz|\(a\^b\)  # 可以通过这个方式预先做好re.sub的准备


import re

str1 = '(9-2)*5+qty/3'
str2 = '(qty+4)/2-(9-2)*5+pq/4'

print(re.sub(r'\(9-2\)\*5', '35', str1))
## '35+qty/3'

print(re.sub(r'\(9-2\)\*5', '35', str2))
## '(qty+4)/2-35+pq/4'


## 复杂字符串先进行 re.escape() 可以看到具体的re识别的代码
items = ['a.b', '3+n', r'x\y\z', 'qty||price', '{n}']

print([re.escape(e) for e in items])
## 返回：['a\\.b', '3\\+n', 'x\\\\y\\\\z', 'qty\\|\\|price', '\\{n\\}']

alt_re = re.compile(r'a\.b|{n}|3\+n|x\\y\\z')

print(alt_re.sub(r'X', '0a.bcd'))
# 返回 '0Xcd'
print(alt_re.sub(r'X', 'E{n}AMPLE'))
# 返回 'EXAMPLE'
print(alt_re.sub(r'X', r'43+n2 ax\y\ze'))
# 返回 '4X2 aXe'



s="432432fgg(1)4u2309hfehhfdshsd(2)f293u238hfedshf()fjisdj(3)23904u2039f0dshf(4)2[u23hfuhdsufnsd(5)dfsogsdofjsnvsfodsfsod(6)........"

a=re.compile(r'\(.\)')
print(a)

print(re.search(a,s))

print(re.findall(a,s))
### ['(1)', '(2)', '(3)', '(4)', '(5)', '(6)']
