# -*- coding: utf-8 -*-
## 密文验证
## 不加盐
import hashlib
m=hashlib.md5()  ## 创建一个md5算法对象，之后无代码提示
m.update(b'1232456')  ## 等价 m.update('123456'.encode('utf-8')) 转化为bety字节
print(m.hexdigest())  ## 对字符串‘123456’加密
print(len(m.hexdigest())) ## 密码长度


m=hashlib.sha1()  ## 创建一个sha1算法对象，之后无代码提示
m.update(b'1232456')  ## 等价 m.update('123456'.encode('utf-8')) 转化为bety字节
print(m.hexdigest())  ## 加密后不变

## 加盐：增加安全性
Salt='gbkdg123'
h = hashlib.md5(bytes(Salt,encoding='utf8'))
h.update(bytes('abc',encoding='utf-8'))
print(h.hexdigest())
print()

## 一段字符串整个读取与分段读取，其加密结果相同 c37da13c5bd22922759cb26b5d8a1878
h = hashlib.md5()
h.update(bytes('abcspring%%%',encoding='utf-8'))
print(h.hexdigest())
h.update(bytes('abc',encoding='utf-8'))
h.update(bytes('spring',encoding='utf-8'))
h.update(bytes('%%%',encoding='utf-8'))
print(h.hexdigest())
# h = hashlib.md5()
# h.update(bytes('abc春天     ',encoding='utf-8'))
# print(h.hexdigest())
print()

## 文件的一致性校验：判断俩个文件内容是否相同的算法
import hashlib
def check(filename):
	md5objection=hashlib.md5()
	with open(filename,'rb') as f:
		content=f.read()
		md5objection.update(content)
	return md5objection.hexdigest()
file1=check('009继承.py')
file2=check('0010多态.py')
print(file1)
print(file2)
if file1!=file2:
	print('文件不相同')
else:
	print('文件相同')

'''
import hashlib
import os

path = r'D:\CentOS 64 位'

def file_md5(path):
    """
    文件校验
    :param path:文件的路径
    :return: 文件的密文
    """
    path_size = os.path.getsize(path)  # 计算文件的大小
    md5 = hashlib.md5()  # 选择md5加密
    with open(path, 'rb') as f:
        while path_size >= 4096:  # 如果文件大小大于4096，进入循环
            cont = f.read(4096)  # 每次读取文件读取4096个字节
            md5.update(cont)
            path_size -= 4096
        else:
            cont = f.read()  # 如果文件小于4096就直接全部读取
            if cont:
                md5.update(cont)
    return md5.hexdigest()  # 返回加密的文件


def jy(path1, path2):
    """
    传送文件去校验
    :param path1:  第一个文件
    :param path2:  第二个文件
    :return: 结果(True,False)
    """
    return file_md5(path1) == file_md5(path2)


path1 = r'D:\CentOS 64 位\CentOS 64 位-Snapshot1.vmem'
path2 = r'D:\CentOS 64 位\CentOS 64 位-Snapshot1 - 副本.vmem'
print(jy(path1, path2))
'''
