# -*- coding: utf-8 -*-
#### asynico 是 Python解决异步io编程的一整套解决方案
## 事件循环，回调，io多路复用
## torando gevent twisted

### 使用 asyncio
# import asyncio
# import time
#
#
# async def get_html(url):          ## 创建一个协程对象
# 	print('start get url')
# 	await asyncio.sleep(3)
# 	print('end get url')
#
# if __name__== '__main__':
# 	start_time=time.time()
# 	loop=asyncio.get_event_loop()   # #  创建一个事件loop
# 	loop.run_until_complete(get_html('https://www.baidu.com')) ## 将协程加入到事件循环loop
# 	print(time.time()-start_time)


###
import asyncio
import time
async def get_html(url):          ## 创建一个协程对象
	print('start get url')
	await asyncio.sleep(3)
	print('end get url')

if __name__== '__main__':
	start_time=time.time()
	loop=asyncio.get_event_loop()   # #  创建一个事件loop
	task=[get_html('https://www.baidu.com/')for i in range(300)]
	loop.run_until_complete(asyncio.wait(task)) ## asyncio.wait:可迭代对象
	print(time.time()-start_time)