# -*- coding: utf-8 -*-
import re

headers_str="""
Accept: application/json, text/javascript, */*; q=0.01
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Connection: keep-alive
Content-Length: 65
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Cookie: _passport_ct=e8b17f158a834424a5e26b8639a491bat1377; _passport_session=3ee92bde5f9b4cb8bc0a5dbd5acb8e095454; RAIL_EXPIRATION=1586676548461; RAIL_DEVICEID=JNEtl_uImaZRsGJq9ArbnfLKUoGGNv06QaA_jG-6e3OJV4T4zIhTc29FU5r9vAHL22kwKJz5r_bszCVY-nk8SqMbDgvxHeGmVlgy-cn0DNwoqJgElb-paSwgiTOZX-pzV9AfXC2bKFlIkRGv4H5IyuIIypsUyHID; BIGipServerpool_passport=401408522.50215.0000; route=495c805987d0f5c8c84b14f60212447d; BIGipServerpassport=854065418.50215.0000; BIGipServerportal=3067347210.17183.0000; BIGipServerotn=3705078026.64545.0000
Host: kyfw.12306.cn
Origin: https://kyfw.12306.cn
Referer: https://kyfw.12306.cn/otn/resources/login.html
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36





"""



pattern='^(.*?): (.*)$'
#          1    2
for line in headers_str.splitlines():
	print(re.sub(pattern, '\'\\1\': \'\\2\',', line))