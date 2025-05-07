import requests
import re

url_main = 'https://dytt.dytt8.net/index.htm'
resp = requests.get(url_main, verify=False)  # verify=False去掉安全验证
resp.encoding = 'gb2312'  # 指定字符集

url_main2 = url_main[0:22]

obj1 = re.compile(r"<p>最新电影更新:.*?<ul>(?P<ul>.*?)</ul>", re.S)
obj2 = re.compile(r"<a href='(?P<ul_chird>.*?)'>", re.S)
obj3 = re.compile(
    r'<meta name=keywords content="(?P<name>.*?)下载">.*?<font color=red>磁力链下载器：<a href="(?P<url>.*?)" target="_blank"  title="qBittorrent">点击下载</a>',
    re.S)
result1 = obj1.finditer(resp.text)
child_herf_list = []

for it in result1:
    ul = it.group('ul')
    # print(ul)

    # 拿到ul里面的li
    # 提取到子页面的链接的地址
    result2 = obj2.finditer(ul)
    for it2 in result2:
        # print(it2.group('ul_chird'))
        child_href = url_main2 + it2.group('ul_chird')
        child_herf_list.append(child_href)  # 把子页面列表加到列表里面

# 提取子页面的内容
for herf in child_herf_list[1:]:
    resp2 = requests.get(herf, verify=False)
    resp2.encoding = 'gb2312'
    # result3 = obj3.search(resp2.text)
    # print(result3.group('name') + "   " + result3.group('url'))
    result3 = obj3.finditer(resp2.text)
    for it3 in result3:
        print(it3.group('name') + "   " + it3.group('url'))
