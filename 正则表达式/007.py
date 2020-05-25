# -*- coding: utf-8 -*-
# @Time : 2020/5/25 9:52
# @Author : Tony
# @File : 007.py
# @Software: PyCharm
# To live is to learn,to learn is to better live.
# Killing time for this

import re

## re.ignorecase: 忽略大小写
print(bool(re.search(r'cat', 'Cat')))
# 返回 False
print(bool(re.search(r'cat', 'Cat', flags=re.IGNORECASE)))
# 返回 True


## re.I:匹配不区分大小写
print(re.findall(r'c.t', 'Cat cot CATER ScUtTLe', flags=re.I))
# 返回 ['Cat', 'cot', 'CAT', 'cUt']

print(re.findall(r'[a-z]+', 'Sample123string42with777numbers', flags=re.I))
# 返回 ['Sample', 'string', 'with', 'numbers']
print(re.split(r'(\d+)','Sample123string42with777numbers'))


## re.S:跨行匹配
print(re.sub(r'the.*ice', r'X', 'Hi there\nHave a Nice Day', flags=re.S))
# 返回 'Hi X Day'


print(re.sub(r'the.*day', r'Bye', 'Hi there\nHave a Nice Day', flags=re.S | re.I))
# 返回 'Hi Bye'


##  re.M:匹配多行中符合条件的字符串
print(re.search(r'^top', "hi hello\ntop spot", flags=re.M))
# 返回 True


s='12 34\n56 78\n90'
print(re.findall(r'^\d+',s,re.MULTILINE))
## ['12', '56', '90']

print(re.search(r'ar$', "spare\npar\ndare", flags=re.M),'\n')
# 返回 'ar'

print('============= re.X ==========')
## re.X	该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解。
rex = re.compile(r'''
         \A(                 # group-1, captures first 3 columns
             (?:[^,]+,){3}   # non-capturing group to get the 3 columns           )
         ([^,]+))            # group-2, captures 4th column
         ''', flags=re.X)

print(rex.sub(r'\1(\2)', '1,2,3,4,5,6,7', count=1))
# 返回 '1,2,3,(4),5,6,7'


print(re.search(r't a', 'cat and dog', flags=re.X))
# 返回 False

print(re.search(r't\ a', 'cat and dog', flags=re.X))
# 返回 True

print(re.findall(r't\ a', 'cat and dog', flags=re.X))
## ['t a']

print(bool(re.search(r't[ ]a', 'cat and dog', flags=re.X)))
# 返回 True

print(re.search(r't[ ]a', 'cat and dog', flags=re.X))

print(bool(re.search(r't\x20a', 'cat and dog', flags=re.X)))
# 返回 True

print(re.search(r'a#b', 'foo a#b 123', flags=re.X)[0])
# 返回 'a'

print(re.search(r'a\#b', 'foo a#b 123', flags=re.X)[0])
# 返回 'a#b'


rex = re.compile(r'\A((?:[^,]+,){3})(?#3-cols)([^,]+)(?#4th-col)')

print(rex.sub(r'\1(\2)', '1,2,3,4,5,6,7', count=1))
# '1,2,3,(4),5,6,7'


print(re.findall(r'Cat[a-z]*\b', 'Cat SCatTeR CATER cAts'))
# 返回 ['Cat']

print(re.findall(r'Cat(?i:[a-z]*)\b', 'Cat SCatTeR CATER cAts'))
# 返回 ['Cat', 'CatTeR']

print(re.findall(r'Cat[a-z]*\b', 'Cat SCatTeR CATER cAts', flags=re.I))
# 返回 ['Cat', 'CatTeR', 'CATER', 'cAts']

print(re.findall(r'(?i)Cat[a-z]*\b', 'Cat SCatTeR CATER cAts'))
# 返回 ['Cat', 'CatTeR', 'CATER', 'cAts']

print(re.findall(r'(?-i:Cat)[a-z]*\b', 'Cat SCatTeR CATER cAts', flags=re.I))
# 返回 ['Cat', 'CatTeR']



print(re.findall(r'\w+', 'fox:αλεπο&#973;'))
# 返回 ['fox', 'αλεπο&#973;']

# restrict matching to only ASCII characters
print(re.findall(r'\w+', 'fox:αλεπο&#973;', flags=re.A))
# 返回 ['fox']

# or, explicitly define the characters to match using character class
print(re.findall(r'[a-zA-Z0-9_]+', 'fox:αλεπο&#973;'))
# 返回 ['fox']

print(bool(re.search(r'[a-zA-Z]', '&#304;&#305;&#383;&#8490;')))
# 返回 False

print(re.search(r'[a-z]+', '&#304;&#305;&#383;&#8490;', flags=re.I))
# 返回 '&#304;&#305;&#383;&#8490;'

print(bool(re.search(r'[a-z]', '&#304;&#305;&#383;&#8490;', flags=re.I | re.A)))
# 返回 False


import regex
print(regex.findall(r'\p{L}+', 'fox:αλεπο&#973;,eagle:αετ&#972;&#962;'))
# 返回 ['fox', 'αλεπο&#973;', 'eagle', 'αετ&#972;&#962;']

# extract all consecutive Greek letters
print(regex.findall(r'\p{Greek}+', 'fox:αλεπο&#973;,eagle:αετ&#972;&#962;'))
# 返回 ['αλεπο&#973;', 'αετ&#972;&#962;']

# extract all words
print(regex.findall(r'\p{Word}+', 'φοο12,βτ_4,foo'))
# 返回 ['φοο12', 'βτ_4', 'foo']

# delete all characters other than letters
# \p{^L} can also be used instead of \P{L}
print(regex.sub(r'\P{L}+', r'', 'φοο12,βτ_4,foo'))
# 返回 'φοοβτfoo'

# to get codepoints for ASCII characters
print([hex(ord(c)) for c in 'fox'])
# 返回 ['0x66', '0x6f', '0x78']
# to get codepoints for Unicode characters
print([c.encode('unicode_escape') for c in 'αλεπο&#973;'])
# 返回 [b'\\u03b1', b'\\u03bb', b'\\u03b5', b'\\u03c0', b'\\u03bf', b'\\u03cd']
print([c.encode('unicode_escape') for c in '&#304;&#305;&#383;&#8490;'])
# 返回 [b'\\u0130', b'\\u0131', b'\\u017f', b'\\u212a']

# character range example using \u
# all english lowercase letters
print(re.findall(r'[\u0061-\u007a]+', 'fox:αλεπο&#973;,eagle:αετ&#972;&#962;'))
# 返回 ['fox', 'eagle']