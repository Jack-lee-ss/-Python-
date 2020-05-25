# 生活不会突变，你要做的只是耐心和积累。人这一辈子没法做太多的事情，所以每一件尽力而为。
# -*- coding: utf-8 -*-
import warnings
warnings.filterwarnings("ignore")
import re

# dot 在这里相当于"省略号" 指代任意字符
print(re.sub(r'c.t', r'X', 'tac tin cat abc;tuv acute'))
# 返回 'taXin X abXuv aXe'

# 只替代..两个dot位之间的字母和 r d 组合
print(re.sub(r'r..d', r'X', 'breadth markedly reported overridesrd  dfdrbnhjkld'))
# 返回 'bXth maXly repoX oveXesrd dfdrbnhjkld'

# # 只替代..两个dot位的字母组合（注意和上述例子的区别）
print(re.sub(r'r..d', r'X', 'breadth markedly reported overides'))
# 返回 'bXth maXly repoX overides'

# 可以将\t换行符也替换掉
print(re.sub(r'2.3', r'8', '42\t35'))
# 返回 '485'


'''
	？：匹配一个或者0个字符串。
  a?b ：含 ab 或者  b 的字符串。
'''
# 记忆 e?ar == (e|)ar == ear|ar
print(re.sub(r'e?ar', r'X', 'far feat flare fear er'))
# 返回 'fX feat flXe fX'

# same as: \bpart?\b == \bpar(t|)\b ==  \bpart\b | \bpar\b
# 可改写成(\bpar(t|)\b 注意?只代表一个值
'''
	fga?\b : 以 a\b(a结尾) 或者 fg\b(fg结尾)
'''
print(re.sub(r'\bpart?\b', r'X', 'par spare part party')) # 以 par 结尾 或者 part 结尾
# 返回 'X spare X party'

# same as: r'\b(re.d|red)\b'
words = ['red', 'read', 'ready', 're;d', 'redo', 'reed']
print([w for w in words if re.search(r'\bre.?d\b', w)])  # \bre(.?d)\b == \bre(.|)d\b == \b(re.d|red)\b
# 返回 ['red', 'read', 're;d', 'reed']

# same as: r'part|parrot'
##  (ab)?v ：(ab)视作一个整体。
print(re.sub(r'par(ro)?t', r'X', 'par part parrot parent'))  # par(ro)?t == par((ro)|)t == par(rot|t) == parrot|part
# 返回 'par X X parent'

# same as: r'part|parrot|parent'
print(re.sub(r'par(en|ro)?t', r'X', 'par part parrot parent'))  # par(en|ro)?t == par((en|ro)|)t == parent|parrot|part
# 返回 'par X X X'

print(re.sub(r'f.?o', r'X', 'foot'))  # f.?o = f(.|)o = f.o|fo
# 返回 'Xt'   因为这种 quantifier 比较greedy ，所以fo 和 foo 在一起的时候 foo被吃掉了

'''
	*  : 0个或者多个(指前面一个字符出现次数)
	
	a* : a字符出现0个或者多个
	
	.  : 匹配任意一个字符或者符号，不包括\n
	
	+  : 一个或者多个(指前面一个字符出现次数)
'''
# ta*r == tr / tar / taar / taaar / taaa...r
print(re.sub(r'ta*r', r'X', 'tr tear tare steer sitaara'))
# 返回 'X tear Xe steer siXa'


# t(e|a)*r == tr / t(e|a)r / t(ee|aa)r / t(ee..|aa..)r
print(re.sub(r't(e|a)*r', r'X', 'tr tear tare steer sitaara'))
# 返回 'X X Xe sX siXa'


# 1*2 = 2 / 12 / 112 / 1112 / 111...2
print(re.sub(r'1*2', r'X', '3111111111125111142'))
# 返回 '3X511114X'


print('========= split() ==========')
### split():分隔符，分隔符前或者后（不包括分隔符本身）
# 以1*2分隔开 和上述的X分割是一样的 但注意最后的一个小尾巴''
print(re.split(r'1*2', '3111111111125111142'))
# 返回 ['3', '511114', '']


# 用这个办法只分割第一个X，第二个X变回原来的2
print(re.split(r'1*2','3111111111125111142',maxsplit=1)) # 只分割第一个符合条件的字符串
# 返回 ['3', '5111142']

print(re.split(r'1*2','3111111111125111142',maxsplit = 2))
## ['3', '511114', '']

# u* =  / u / uu / uuu / uuu... 这里有个效果就是他直接用第一个''分割
print(re.split(r'u*', 'cloudy'))
# 返回 ['clo', 'dy']


print(re.sub(r'ta+r', r'X', 'tr tear tare steer sitaara'))
# 返回 'tr tear Xe steer siXa'

print(re.sub(r't(e|a)+r', r'X', 'tr tear tare steer sitaara'))  # t(e|a)+r = t(e|a)r / t(ee|aa)r) / ...
# 返回 'tr X Xe sX siXa'

print(re.sub(r'1+2', r'X', '3111111111125111142'))  # 1+2 = 12 / 112 / 1112 / 111...2
# 返回 '3X5111142'

print(re.split(r'1+', '3111111111125111142'))  # 1+ = 1 / 11 / 111 / 111...
# 返回 ['3', '25', '42']
print(re.split(r'u+', 'cloudy'))  # u+ = u / uu / uuu / uuu...
# 返回 ['clo', 'dy']

'''
	{m,n}       match m to n times  b{n,m}量词可以重复前面匹配的字符b n-m次，至少n次，最多m次。
	{m,}        match at least m times
	{,n}        match up to n times (including 0 times)
	{n}         match exactly n times
'''
print('========= {m,n} ======')
demo = ['abc', 'ac', 'adc', 'abbc', 'xabbbcz', 'abbbbc', 'bc', 'abbbbbc']

# ab{1,4}c = abc / abbc / abbbc / abbbbc
# 匹配 b出现的次数 {1,4},最少1次，最多4次。
print([w for w in demo if re.search(r'ab{1,4}c', w)])
# 返回 ['abc', 'abbc', 'xabbbcz', 'abbbbc']

# ab{3,}c = abc / abbc / abbbc / ... 无穷
print([w for w in demo if re.search(r'ab{3,}c', w)])
# 返回 ['xabbbcz', 'abbbbbc']

# ab{,2}c = ac / abc / abbc
print([w for w in demo if re.search(r'ab{,2}c', w)])
# 返回 ['abc', 'ac', 'abbc']

# ab{3}c = abbbc
print([w for w in demo if re.search(r'ab{3}c', w)])
# 返回 ['xabbbcz']

print(bool(re.search(r'Error.*valid', 'Error: not a valid input')))
# 返回 True  # any number of characters between Error and valid # .* =  / . / .. / ... / .... 匹配任意无限多的字符

print(bool(re.search(r'Error.*valid', 'Error: key not found')))
# 返回 False

print(re.sub(r'c.*t', r'X', 'tac tin cat abc;tuv acute'))  # 拿第一个例子做对比架设了一个*
# 返回 'taXe' 而不是 'taXin X abXuv aXe'
# c.t 是c后面发现第一个t就结算；
# c.*t 是从第一个c开始一直到发现到最后一个t才结算
# 贪婪模式


print(re.sub(r'\\?<', r'\<', r'blah \< foo < bar \< blah < baz'))
# 返回 blah \< foo \< bar \< blah \< baz
# 提示 \\?< = \(\|)< = \\<|\< == 实际效果"\<|<" 即对符号 \< 和< 优先是\< 其次是<

print(re.sub(r'\\<', r'<', r'blah \< foo < bar \< blah < baz'))  # 对应上述的变形，如果单纯地将'<'转变成'\<'
# 返回 blah < foo < bar < blah < baz  说明上述式子的 \\< == 实际效果"\<"

# say goodbye to r'handful|handy|hand' shenanigans（恶作剧）
print(re.sub(r'hand(y|ful)?', r'X', 'hand handy handful'))
# 返回 'X X X'
# 提示 hand(y|ful)? = hand((y|ful)|) = hand(y|ful)|hand = handy|handful|hand
# 掌握速记 'hand'本身 + 不同后缀(y|ful)的组合

print('=========== 贪婪模式 ==========')
sentence = 'that is quite a fabricated tale'

print(re.sub(r't.*a', r'X', sentence, count=1))  # t.*a = ta / t.a / t..a / ... 因为是greedy, 所以吃the longest one
# 返回 'Xle'

print(re.sub(r't.*a', r'X', 'star', count=1))  # count 在这里不起作用
# 返回 'sXr'

print(re.sub(r't.*a.*q.*f', r'X', sentence, count=1))  # 如果存在多个.*则按count的方式结算
# 返回 'Xabricated tale'

print(re.sub(r't.*a.*u', r'X', sentence, count=1))  # 如果存在多个.*则按count的方式结算
# 返回 'Xite a fabricated tale'


print("================= 非贪婪模式 ============")
print(re.sub(r'f.??o', r'X', 'foot', count=1))  # f.?o = f(.|)o = f.o|fo 如果是greedy 那么就优先f.o 但加上了?则优先匹配fo/f.o
# 返回 'Xot'

print(re.sub(r'f.?o', r'X', 'foot', count=1))  # 对比上述 优先匹配f.o
# 返回 'Xt'

print(re.sub(r'f.??o', r'X', 'frost', count=1))  # 这种情况肯定匹配的是f.o
# 返回 'Xst'

print(re.sub(r'f.??o', r'X', 'frrost', count=1))  # 尽管这种情况肯定匹配的是f.o，但是无法匹配到合适的字符，所以按原文返回
# 返回 'frrost'

print(re.sub(r'.{2,5}?', r'X', '123456789', count=1))  # .{2,5}? = .{2,5} = .. / ... / .... / ..... 由于存在? 则优先匹配..
# 返回 'X3456789'


sentence = 'that is quite a fabricated tale'

# r't.*?a' will always match from first 't' to first 'a'
print(re.sub(r't.*?a', r'X', sentence, count=1))  # 由于存在? 则优先匹配符合条件的第一个t.*a
# 返回 'Xt is quite a fabricated tale'

# matching first 't' to first 'a' for t.*?a won't work for this case
# so, engine will move forward until .*?f matches and so on
print(re.sub(r't.*?a.*?f', r'X', sentence, count=1))  # t.*?a.*?f 匹配第一个t\a\f 在本题中 效果和t.*?f效果一样
# 返回 'Xabricated tale'



# import regex 一下的函数均用的是regex包里的函数
## https://www.cnblogs.com/animalize/p/4949219.html

import regex as re
demo = ['abc', 'ac', 'adc', 'abbc', 'xabbbcz', 'bbb', 'bc', 'abbbbbc']

# functionally equivalent greedy and possessive versions
print([w for w in demo if re.search(r'ab*c', w)])  # ab*c = ac\ abc \ abbc \ abbb..c
# 返回 ['abc', 'ac', 'abbc', 'xabbbcz', 'abbbbbc']

print([w for w in demo if re.search(r'ab*+c', w)])  # ab*+c 效果和上述一样，区别见下文
# 返回 ['abc', 'ac', 'abbc', 'xabbbcz', 'abbbbbc']

# different results
print(re.sub(r'f(a|e)*at', r'X', 'feat ft feaeat'))  # f(a|e)*at = fX*at (假设(a|e)=X) = fat \ fa..at \ feaeat greedy
# 返回 'X ft X'

print(re.sub(r'f(a|e)*+at', r'X', 'feat ft feaeat'))
# 返回 'feat ft feaeat'

print(re.sub(r'f(a|e)*+t', r'X', 'feat ft feaeat'))  # 和上述 式子做个比较发现额外的一个"a"干扰了整个判断
# 返回 X X X


# same as: r'(b|o)++'
print(re.sub(r'(?>(b|o)+)', r'X', 'abbbc foooooot'))  # ?>(b|o)+) = (?>pat); pat = (b|o)+ = bbb...|ooo...
# 返回 'aXc fXt'

# same as: r'f(a|e)*+at'
print(re.sub(r'f(?>(a|e)*)at', r'X', 'feat ft feaeat'))  # f(?>(a|e)*)at = f(?>pat)at; pat = (a|e)* = aaa...|eee...
# 返回 'feat ft feaeat'