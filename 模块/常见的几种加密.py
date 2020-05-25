# 生活不会突变，你要做的只是耐心和积累。人这一辈子没法做太多的事情，所以每一件尽力而为。
# -*- coding: utf-8 -*-

## Base64 加密
'''
python本身默认编码为unicode
#所有编码转换时都需通过unicode
msg = "北京"
print(msg.encode(encoding = "utf-8"))#unicode编码转换为utf-8编码
print(msg.encode(encoding = "utf-8").decode(encoding = "utf-8"))#unicode编码转换为utf-8编码，再转化为unicode编码

'''
### Base64 加密
# 加密：可打印字符包括字母A-Z/a-z/数组0-9/ 加号’+’斜杠’/’ 这样共有62个字符
import base64
s='12314dfg'
s=s.encode('utf-8')   ## 字符串转化成二进制，在加密。
m=base64.b64encode(s)
print(m)

# 解密
s=['Wk9vY0g=', 'eFZoQkY=', 'aXdMYXI=', 'dHlwZQ==', 'c3Vic3RyaW5n', 'YmN6V24=', 'T2NlbWk=', 'dGV4dEJhc2VsaW5l', 'VXFKalU=', 'ZmlsbFN0eWxl', 'UXd3d2c=', 'ZmlsbFRleHQ=', 'amd1RFk=', 'Zm9udA==', 'SHptQ1Q=', 'VGpLU3I=', 'ZGlzcGxheQ==', 'WWtaZE8=', 'dG9EYXRhVVJM', 'TkFoVUc=', 'ZmlsbFJlY3Q=']
l=[]
for i in s:
	x=base64.b64decode(i)   ## 对字符串解码，转化成 byte
	l.append((x.decode('utf-8')).replace('b',''))  ## 对 byte 转化为字符串后再解码成utf-8
print(l)

## md5 加密
'''
1、压缩性：任意长度的数据，算出的MD5值长度都是固定的。

2、容易计算：从原数据计算出MD5值很容易。

3、抗修改性：对原数据进行任何改动，哪怕只修改1个字节，所得到的MD5值都有很大区别。

4、强抗碰撞：已知原数据和其MD5值，想找到一个具有相同MD5值的数据（即伪造数据）是非常困难的。
'''

import hashlib

s='https://www.baidu.com/'
m=hashlib.md5()
m.update(s.encode('utf-8'))
print(m.digest())   ## b'\xe8\x1c\x1fWIT\\_}${:\x10\x0f\xfeb' 2进制
print(m.hexdigest()) # e81c1f5749545c5f7d247b3a100ffe62  16进制


#### md5() 加盐算法

## 分开加盐，加密 等价 一起加密
#  静态盐  ------------------- 密文不变
salt='python+js'
m=hashlib.md5()
m.update((salt+'https://www.baidu.com/').encode('utf-8'))
print(m.hexdigest()) # 66abd8f6766c07198add50632daa6351


s='python+js'
n=hashlib.md5()
n.update(s.encode('utf-8'))
n.update(('https://www.baidu.com/').encode('utf-8'))
print(n.hexdigest()) # 66abd8f6766c07198add50632daa6351
print()


## 动态盐  ------------- 密文一直变化
import random
import time
salt1=str(random.randint(0,100))
salt2=str(time.time())
m=hashlib.md5()
m.update((salt1+salt2+'https://www.baidu.com/').encode('utf-8'))
print(m.hexdigest())



'''
  		验证账号与密码
		import hashlib

		SALT = b'2erer3asdfwerxdf34sdfsdfs90'
		def md5(pwd):
			# 实例化对象
			obj = hashlib.md5(SALT)
			# 写入要加密的字节
			obj.update(pwd.encode('utf-8'))
			# 获取密文
			return obj.hexdigest()

		user = input("请输入用户名:")
		pwd = input("请输入密码:")
		if user == 'oldboy' and md5(pwd) == 'c5395258d82599e5f1bec3be1e4dea4a':
			print('登录成功')
		else:
			print('登录失败')
'''

## sha1加密（加密不可逆）
# SHA1的全称是Secure Hash Algorithm(安全哈希算法)
## SHA1基于MD5，加密后的数据长度更长。它对长度小于264的输入，产生长度为160bit的散列值。比MD5多32位。因此，比MD5更加安全，但SHA1的运算速度就比MD5要慢了。使用方法和MD5其实是一样的

import hashlib
s='https://www.baidu.com/'
m=hashlib.sha1()
m.update(s.encode('utf-8'))
print(m.hexdigest())
print('===============')


## 进制转换，只接受数字
print(hex(-123))      # hex():整型十进制转十六进制
print((-1.456).hex()) # 浮点型转化成十六进制

print(bin(-45))        # 十进制转化为二进制，整型或者长整型

print(oct(-333432))    #  十进制转化为八进制，整型

print(chr(98))       # 整型转化成ASCII码表中的单个字符

print(ord('b'))      # 单个字符转化成整数

print(int(0x200))    # 十六进制转化为十进制


## binascii 模块 ：进制与字符串之间的转换
import binascii
s='abcded'                             ## 注：字符串长度是偶数个  字符串-----十六进制
print(binascii.a2b_hex(s))              # 字符串转化为十六进制
print(binascii.a2b_hex(b'abcded'))      # 同上

print(binascii.b2a_hex(b'abcded'))      # b'616263646564', 字符串---二进制---十六进制
print()

## AES()加密（需要密钥才能解密）
##  AES加密为对称密钥加密，加密和解密都是用同一个解密规则，AES加密过程是在一个4×4的字节矩阵上运作，这个矩阵又称为"状态(state)"，因为密钥和加密块要在矩阵上多次的迭代，置换，组合，所以对加密快和密钥的字节数都有一定的要求，AES密钥长度的最少支持为128、192、256，加密块分组长度128位。这种加密模式有一个最大弱点：甲方必须把加密规则告诉乙方，否则无法解密。保存和传递密钥，就成了最头疼的问题。 

## 密钥（16，24, 32位），偏移量（位数同密钥，不足补\0, CBC有偏移量；ECB没有偏移量），填充方式（pkcs7padding）

from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import algorithms

# 如果text不足16位的倍数就用空格补足为16位
def add_to_16(text):
	if len(text.encode('utf-8')) % 16!=0:
		add = 16 - (len(text.encode('utf-8')) % 16)
	else:
		add = 0
	text = text + ('\0' * add)
	return text.encode('utf-8')


def pkcs7_padding(data):

	padder = padding.PKCS7(algorithms.AES.block_size).padder()

	padded_data = padder.update(data) + padder.finalize()

	return padded_data

# 加密函数
def encrypt(strings,mode):
	key = '625202f9149e061d'.encode('utf-8')
	iv = '5efd3f6060e20330'.encode('utf-8')
	text = add_to_16(strings)
	if mode==AES.MODE_CBC:
		cryptos = AES.new(key, mode, iv)
	else:
		cryptos = AES.new(key, mode)
	data=pkcs7_padding(text)
	cipher_text = cryptos.encrypt(data)
	# 因为AES加密后的字符串不一定是ascii字符集的，输出保存可能存在问题，所以这里转为16进制字符串
	return b2a_hex(cipher_text)


# 解密后，去掉补足的空格用strip() 去掉
def decrypt(e,text_mode):
	key = '625202f9149e061d'.encode('utf-8')
	iv = '5efd3f6060e20330'.encode('utf-8')
	if text_mode==AES.MODE_CBC:
		cryptos = AES.new(key, text_mode, iv)
	else:
		cryptos = AES.new(key, text_mode)
	plain_text = cryptos.decrypt(a2b_hex(e))
	return bytes.decode(plain_text).rstrip('\0')

def choose_mode(num):
	m = {
		1: AES.MODE_ECB,
		2: AES.MODE_CBC
	}
	mode = m[num]
	return mode

if __name__ == '__main__':
	mode=int(input('请选择加密模式：1(AES.MODE_ECB) 或者 2(AES.MODE_CBC):  '))
	strings=input('输入要加密的文字：')
	text_mode=choose_mode(mode)
	print('加密模式%s,填充方式默认PKCS7'%text_mode)
	e = encrypt(strings,text_mode)  # 加密
	print(e)
	d = decrypt(e,text_mode)  # 解密
	print("加密:", str(e).replace('b',''))
	print("解密:", d)
	

######  RSA():加密

import rsa
import base64
## 生成公私钥，并且保存
pubkey, privkey=rsa.newkeys(1024)  ## 生成公钥，私钥
pub=pubkey.save_pkcs1()             # 转换再保存公钥
pri=privkey.save_pkcs1('PEM')       # 转换再保存私钥，默认参数是 'PEM'

with open('pubkey.pem','wb')as f1, open('privkey.pem','wb')as f2:
	f1.write(pub)
	f2.write(pri)

## 公钥加密，私钥解密

with open('pubkey.pem','r')as f1,open('privkey.pem','r')as f2:
	pub=f1.read()
	pri=f2.read()
	pubkey=rsa.PublicKey.load_pkcs1(pub)         # 还原为原来的状态
	privkey=rsa.PrivateKey.load_pkcs1(pri)

s='sfsgsgs335'
encrypt_s=base64.b64encode(rsa.encrypt(s.encode('utf-8'),pubkey))  ## 字符串转化为二进制，在加密
print('加密结果：',str(encrypt_s).replace('b',''))
decrypt_s=rsa.decrypt(base64.b64decode(encrypt_s),privkey).decode('utf-8')
print('解密结果： ',decrypt_s)    ## 先解码二进制转化为字符串，在解密

