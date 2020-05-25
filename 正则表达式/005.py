# 生活不会突变，你要做的只是耐心和积累。人这一辈子没法做太多的事情，所以每一件尽力而为。
# -*- coding: utf-8 -*-

import  re

words = ['cute', 'cat', 'cot', 'coat', 'cost', 'scuttle']

# same as: r'cot|cut' or r'c(o|u)t'
print([w for w in words if re.search(r'c[ou]t', w)])
# 返回 ['cute', 'cot', 'scuttle']

# same as: r'(a|e|o)+t'
print(re.sub(r'[aeo]+t', r'X', 'meeting cute boat site foot'))
# 返回 'mXing cute bX site fX'

## (0-9)匹配'0-9'本身。[0-9]*匹配数字（注意后面有*，可以为空）
## [0-9]+匹配数字(注意后面有+，不可以为空)，
print(re.findall(r'[0-9]+', 'Sample123string42with777numbers'))
# 返回 ['123', '42', '777']

print(re.findall(r'\b[a-z0-9]+\b', 'coat Bin food tar12 best'))
# 返回 ['coat', 'food', 'tar12', 'best']

print(re.findall(r'\b[p-z][a-z]*\b', 'coat tin food put stoop best'))
# 返回 ['tin', 'put', 'stoop']

print(re.findall(r'\b[a-fp-t]+\b', 'coat tin food put stoop best'))
# 返回 ['best']


print(re.findall(r'\b[12][0-9]\b', '23 154 12 26 98234'))
# 返回 ['23', '12', '26']

# numbers >= 100, 数字位数至少3位。
print(re.findall(r'\b[0-9]{3,}\b', '23 154 12 26 98234'))
# 返回 ['154', '98234']

# numbers >= 100 if there are leading zeros
print(re.findall(r'\b0*[1-9][0-9]{2,}\b', '0501 035 154 12 26 98234'))
# 返回 ['0501', '154', '98234']


# numbers < 350
m_iter = re.finditer(r'[0-9]+', '45 349 651 593 4 204')
print([m[0] for m in m_iter if int(m[0]) < 350])
# 返回 ['45', '349', '4', '204']


def num_range(s):
	return '1' if 200 <= int(s[0]) <= 650 else '0'

print(re.sub(r'[0-9]+', num_range, '45 349 651 593 4 204'))
# 返回 '0 1 0 1 0 1'


# all non-digits
print(re.findall(r'[^0-9]+', 'Sample123string42with777numbers'))
# 返回 ['Sample', 'string', 'with', 'numbers']

# remove first two columns where : is delimiter
print(re.sub(r'\A([^:]+:){2}', r'', 'foo:123:bar:baz', count=1))
# 返回 'bar:baz'

# deleting characters at end of string based on a delimiter
print(re.sub(r'=[^=]+\Z', r'', 'foo=42; baz=123', count=1))
# 返回 'foo=42; baz'


words = ['tryst', 'fun', 'glyph', 'pity', 'why']

print([w for w in words if re.search(r'\A[^aeiou]+\Z', w)])
# 返回 ['tryst', 'glyph', 'why']

print([w for w in words if not re.search(r'[aeiou]', w)])
# 返回 ['tryst', 'glyph', 'why']


print(re.findall(r'\b[a-z-]{2,}\b', 'ab-cd gh-c 12-423'))
# 返回 ['ab-cd', 'gh-c']

print(re.findall(r'\b[a-z\-0-9]{2,}\b', 'ab-cd gh-c 12-423'))
# 返回 ['ab-cd', 'gh-c', '12-423']

# ^ should be other than first character or escaped using \
print(re.findall(r'a[+^]b', 'f*(a^b) - 3*(a+b)'))
# 返回 ['a^b', 'a+b']
print(re.findall(r'a[\^+]b', 'f*(a^b) - 3*(a+b)'))
# 返回 ['a^b', 'a+b']

# [ can be escaped with \ or placed as last character
# ] can be escaped with \ or placed as first character
print(re.search(r'[a-z\[\]0-9]+', 'words[5] = tea')[0])
# 返回 'words[5]'
# \ should be escaped using \
print(re.search(r'[a\\b]+', r'5ba\babc2')[0])
# 返回 ba\bab

'''Escape sequence character sets
\w is similar to [a-zA-Z0-9_] for matching word characters (recall the definition for word boundaries)
\d is similar to [0-9] for matching digit characters
\s is similar to [ \t\n\r\f\v] for matching whitespace characters
'''

print(re.split(r'\d+', 'Sample123string42with777numbers'))
# 返回 ['Sample', 'string', 'with', 'numbers']
print(re.findall(r'\d+', 'foo=5, bar=3; x=83, y=120'))
# 返回 ['5', '3', '83', '120']

print(''.join(re.findall(r'\b\w', 'sea eat car rat eel tea')))
# 返回 'secret'
print(re.findall(r'[\w\s]+', 'tea sea-pit sit-lean\tbean'))
# 返回 ['tea sea', 'pit sit', 'lean\tbean']

'''And negative logic strikes again, use \W, \D, and \S respectively for their negated character class.'''

print(re.sub(r'\D+', r'-', 'Sample123string42with777numbers'))
# 返回 '-123-42-777-'

print(re.sub(r'\W+', r'', 'foo=5, bar=3; x=83, y=120'))
# 返回 'foo5bar3x83y120'

print(re.findall(r'\S+', '   1..3  \v\f  foo_baz 42\tzzz   \r\n1-2-3  '))
# 返回 ['1..3', 'foo_baz', '42', 'zzz', '1-2-3']