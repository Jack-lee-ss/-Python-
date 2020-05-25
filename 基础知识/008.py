### 电影天堂爬取
# import requests
# from lxml import etree
#
# BASE_DOMAIN = 'https://www.dytt8.net'
# HEADERS = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
# }
#
#
# def get_detail_urls(url):
#     response = requests.get(url, headers=HEADERS)
#     text = response.content.decode(encoding='gbk', errors='ignore')
#     html = etree.HTML(text)
#     detail_urls = html.xpath('//table[@class="tbspan"]//a/@href')
#     detail_urls = map(lambda url: BASE_DOMAIN+url, detail_urls)
#     #print(detail_urls)
#     return detail_urls
#
#
# def get_detail_info(url):
#     movie = {}
#     response = requests.get(url, headers=HEADERS)
#     text = response.content.decode(encoding='gbk', errors='ignore')
#     html = etree.HTML(text)
#     movie['title'] = html.xpath('//div[@class="title_all"]//font/text()')[0]
#     img = html.xpath("//div[@id='Zoom']//img/@src")
#     movie['cover'] = img
#     #movie['screenshot'] = img[1]
#     infos = html.xpath('//div[@id="Zoom"]//p/text()')
#     #print(infos)
#     # 提取信息
#     is_actors = False
#     actors = []
#     for info in infos:
#         # print(info)
#         if info.startswith('◎年　　代'):
#             movie['year'] = info.replace("◎年　　代", "").strip()
#         elif info.startswith('◎产　　地'):
#             movie['country'] = info.replace("◎产　　地", "").strip()
#         elif info.startswith('◎类　　别'):
#             movie['category'] = info.replace("◎类　　别", "").strip()
#         elif info.startswith('◎豆瓣评分'):
#             movie['douban_rating'] = info.replace("◎豆瓣评分", "").strip()
#         elif info.startswith('◎片　　长'):
#             movie['duration'] = info.replace("◎片　　长", "").strip()
#         elif info.startswith('◎导　　演'):
#             movie['director'] = info.replace("◎导　　演", "").strip()
#         elif info.startswith('◎主　　演'):
#             actors = [info.replace("◎主　　演", "").strip()]
#             is_actors = True
#         elif is_actors:
#             if info.startswith('◎'):
#                 is_actors = False
#                 movie['actors'] = actors
#                 continue
#             actors.append(info.strip())
#     movie['download'] = html.xpath("//div[@id='Zoom']//tbody//a/text()")
#     movie['magnet'] = html.xpath("//div[@id='Zoom']//a/@href")[0]
#
#     return movie
#
#
# def spider():
#     base_url = 'https://www.dytt8.net/html/gndy/dyzz/list_23_{}.html'
#     movies = []
#     for i in range(1, 2):
#         url = base_url.format(i)
#         detail_urls = get_detail_urls(url)
#         for detail_url in detail_urls:
#             # 对详情页提取信息
#             # print(detail_url)
#             movies.append(get_detail_info(detail_url))
#     print(movies)
#
#
# if __name__ == '__main__':
#     spider()
    


print('====================================================')


import requests
from lxml import etree

# 全局变量
BASE_DOMAIN = 'http://www.ygdy8.net'
HEADERS = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36 ',
    'Referer': 'https://movie.douban.com/',
    'Accept-Encoding': 'zip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Host': 'www.dytt8.net'
}


def get_detail_urls(url):
    # requests库默认会使用自己猜测的编码方式将抓取的网页解码，然后再存储到text属性上去，
    # 在此网站中编码方式为gb2312,所以会出现乱码
    response = requests.get(url, headers=HEADERS)
    text = response.content.decode('gbk')  # 自定义gbk解码方式
    # text = response.text
    html = etree.HTML(text)
    detail_urls = html.xpath("//table[@class='tbspan']//a/@href")
    detail_urls = map(lambda url: BASE_DOMAIN + url, detail_urls)  # detail_url为一个列表，遍历这个列表url=detail_urls[index]执行lambda组成想列表
    return detail_urls


# 传入详情地址进行解析
def parse_detail_page(url):
    movie = {}
    response = requests.get(url, headers=HEADERS)
    text = response.content.decode('gbk')
    html = etree.HTML(text)
    title = html.xpath("//div[@class='title_all']//font[@color='#07519a']/text()")[0]
    movie['title'] = title

    zoomE = html.xpath("//div[@id='Zoom']")[0]  # 获取div
    imgs = html.xpath(".//img/@src")  # 图片
    cover = imgs[0]  # 封面图
    screenshot = imgs[1]  # 截图
    movie['cover'] = cover
    movie['screenshot'] = screenshot

    infos = zoomE.xpath(".//text()")  # 信息
    #print(infos)

    # 定义工具函数
    def parse_info(info, rule):
        return info.replace(rule, '').strip()  # 去除多余字符和空格

    for index, info in enumerate(infos):
        #print(info)
        if info.startswith('◎年　　代'):  # 以该字符串开始
            info = parse_info(info, '◎年　　代')
            movie['year'] = info
        elif info.startswith('◎产　　地'):
            info = parse_info(info, '◎产　　地')
            movie['country'] = info
        elif info.startswith('◎类　　别'):
            info = parse_info(info, '◎类　　别')
            movie['category'] = info
        elif info.startswith('◎豆瓣评分'):
            info = parse_info(info, '◎豆瓣评分')
            movie['douban_rating'] = info
        elif info.startswith('◎片    长'):
            info = parse_info(info, '◎片    长')
            movie['duration'] = info
        elif info.startswith('◎导　　演'):
            info = parse_info(info, '◎导　　演')
            movie['director'] = info
        elif info.startswith('◎主    演'):  # 主演是一个列表
            info = parse_info(info, '◎主    演')
            actors = [info]
            for x in range(index+1, len(infos)):  #
                actor = infos[x].scrip()
                if actor.startswith('◎'):
                    break
                actors.append(actor)
            movie['actors'] = actors
        elif info.startswith('◎简   介'):
            info = parse_info(info, '◎简   介')
            for x in range(index + 1, len(infos)):  #
                profile = infos[x].scrip()
                movie['profile'] = profile
    download_url = html.xpath("//td[@bgcolor='#fdfddf']/a/@href")[0]
    movie['download_url'] = download_url
    return movie


def spider():
    base_url = 'http://www.ygdy8.net/html/gndy/dyzz/list_23_{}.html'
    movies = []
    for x in range(0, 3):  # 获取7页
        url = base_url.format(x)
        detail_urls = get_detail_urls(url)  # 获得详情页面的地址
        for detail_url in detail_urls:  # 遍历每页所有电影url
            movie = parse_detail_page(detail_url)
            movies.append(movie)
            #print(movies)
    # print(movies)


if __name__ == '__main__':
    spider()