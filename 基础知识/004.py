###  模拟滑动，点击事件

# coding:utf-8
# from selenium import webdriver
# from selenium.webdriver import ActionChains
# import time
#
# a=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
# browser=webdriver.Chrome(executable_path=a)
# try:
#     browser.get("http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
#     browser.maximize_window()
#
#     browser.switch_to.frame('iframeResult')
#
#     source = browser.find_element_by_id('draggable')
#     target = browser.find_element_by_id('droppable')
#
#     print(source)
#     print(target)
#     actions = ActionChains(browser)
#     actions.drag_and_drop(source, target)
#     actions.perform()
#
#     alert = browser.switch_to.alert
#     print(alert)
#     time.sleep(3)
#     alert.dismiss()
#
#     time.sleep(5)
# except Exception as e:
#     print(e)
# finally:
#     browser.quit()
#     print('OK')


#####  拖动滚动条
from selenium import webdriver
from selenium.webdriver import ActionChains  # 引入ActionChains鼠标操作类
from selenium.webdriver.common.keys import Keys  # 引入keys类操作
import time

# a=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
# browser=webdriver.Chrome(executable_path=a)
# browser.get('http://www.baidu.com')
# print('现在将浏览器最大化')
# browser.maximize_window()
# browser.find_element_by_id('kw').send_keys('python')
# #now_window=browser.current_window_handle
# print(browser.title)
# browser.find_element_by_id('su').click()
# time.sleep(2)
# js="var q=document.documentElement.scrollTop=100000" ### 滚轴拉倒底部
# browser.execute_script(js)
# time.sleep(1)
# js="var q=document.documentElement.scrollTop=0"  ### 拉至顶部
# browser.execute_script(js)
# time.sleep(1)
# # for i in range(1,10,2):
# # 	js="window.scrollTo(i*60,600)"
# # 	time.sleep(1)
# # 	browser.execute_script(js[0])
# js="window.scrollTo(80,744)"
# browser.execute_script(js)
# print(browser.title)
# print(browser.get_window_size())

# # -*- coding: utf-8 -*-
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# #定义一个taobao类
# class taobao_infos:
#
#     #对象初始化
#     def __init__(self):
#         url = 'https://login.taobao.com/member/login.jhtml?redirectURL=https%3A%2F%2Fwww.taobao.com%2F'
#         self.url = url
#
#         options = webdriver.ChromeOptions()
#         options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2}) # 不加载图片,加快访问速度
#         options.add_experimental_option('excludeSwitches', ['enable-automation']) # 此步骤很重要，设置为开发者模式，防止被各大网站识别出来使用了Selenium
#
#         self.browser = webdriver.Chrome(executable_path=chromedriver_path, options=options)
#         self.wait = WebDriverWait(self.browser, 10) #超时时长为10s
#
#
#     #登录淘宝
#     def login(self):
#
#         # 打开网页
#         self.browser.get(self.url)
#
#         # 等待 密码登录选项 出现
#         password_login = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.qrcode-login > .login-links > .forget-pwd')))
#         password_login.click()
#
#         # 等待 微博登录选项 出现
#         weibo_login = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.weibo-login')))
#         weibo_login.click()
#
#         # 等待 微博账号 出现
#         weibo_user = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.username > .W_input')))
#         weibo_user.send_keys()
#
#         # 等待 微博密码 出现
#         weibo_pwd = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.password > .W_input')))
#         weibo_pwd.send_keys()
#
#         # 等待 登录按钮 出现
#         submit = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.btn_tip > a > span')))
#         submit.click()
#
#         # 直到获取到淘宝会员昵称才能确定是登录成功
#         taobao_name = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.site-nav-bd > ul.site-nav-bd-l > li#J_SiteNavLogin > div.site-nav-menu-hd > div.site-nav-user > a.site-nav-login-info-nick ')))
#         # 输出淘宝昵称
#         print(taobao_name.text)
#
#
# if __name__ == "__main__":
# 	chromedriver_path = r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'  # 改成你的chromedriver的完整路径地址
# 	weibo_username = "改成你的微博账号"  # 改成你的微博账号
# 	weibo_password = "改成你的微博密码"  # 改成你的微博密码
#
# 	a = taobao_infos()
# 	a.login()  # 登录


## 登录QQ
# encoding=utf8

from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

url = 'https://xui.ptlogin2.qq.com/cgi-bin/xlogin?&low_login=0&appid=636014201&target=self&border_radius=1&maskOpacity=40&s_url=http%3A//www.qq.com/qq2012/loginSuccess.htm'


def get_track(distance):
    track = []
    current = 0
    mid = distance * 3 / 4
    t = 0.2
    v = 0
    while current < distance:
        if current < mid:
            a = 2
        else:
            a = -3
        v0 = v
        v = v0 + a * t
        move = v0 * t + 1 / 2 * a * t * t
        current += move
        track.append(round(move))
    return track


def main():
    driver = webdriver.Chrome()
    driver.set_window_position(900, 10)
    driver.get(url)
    # 检测id为"switcher_plogin"的元素是否加在DOM树中，如果出现了才能正常向下执行
    element = WebDriverWait(driver, 5, 0.5).until(
        EC.presence_of_element_located((By.ID, "switcher_plogin"))
    )
    element.click()

    sleep(1)
    # 输入用户名和密码
    driver.find_element_by_id('u').clear()
    driver.find_element_by_id('u').send_keys('123456')
    driver.find_element_by_id('p').clear()
    driver.find_element_by_id('p').send_keys('ccccc')
    sleep(1)
    # 点击登录
    driver.find_element_by_id('login_button').click()

    sleep(5)

    # 切换iframe
    try:
        iframe = driver.find_element_by_xpath('//iframe')
    except Exception as e:
        print('get iframe failed: ', e)
    sleep(2)  # 等待资源加载
    driver.switch_to.frame(iframe)

    # 等待图片加载出来
    WebDriverWait(driver, 5, 0.5).until(
        EC.presence_of_element_located((By.ID, "tcaptcha_drag_button"))
    )
    try:
        button = driver.find_element_by_id('tcaptcha_drag_button')
    except Exception as e:
        print('get button failed: ', e)

    sleep(1)
    # 开始拖动 perform()用来执行ActionChains中存储的行为
    flag = 0
    distance = 195
    offset = 5
    times = 0
    while 1:
        action = ActionChains(driver)
        action.click_and_hold(button).perform()
        action.reset_actions()  # 清除之前的action
        print(distance)
        track = get_track(distance)
        for i in track:
            action.move_by_offset(xoffset=i, yoffset=0).perform()
            action.reset_actions()
        sleep(0.5)
        action.release().perform()
        sleep(5)

        # 判断某元素是否被加载到DOM树里，并不代表该元素一定可见
        try:
            alert = driver.find_element_by_class_name('tcaptcha-title').text
        except Exception as e:
            print
            'get alert error: %s' % e
            alert = ''
        if alert:
            print
            u'滑块位移需要调整: %s' % alert
            distance -= offset
            times += 1
            sleep(5)
        else:
            print
            '滑块验证通过'
            flag = 1
            driver.switch_to.parent_frame()      # 验证成功后跳回最外层页面
            break

    sleep(2)
    driver.quit()
    print
    "finish~~"
    return flag


if __name__ == '__main__':
    main()