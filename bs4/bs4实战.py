# 1 拿到主页面的源代码，然后提取到子页面的链接地址，href
# 2 通过href进入子页面，拿到图片的下载的地址
# 下载图片
from bs4 import BeautifulSoup
import requests

url = 'https://www.umei.cc/bizhitupian/xiaoqingxinbizhi/'
resp = requests.get(url)
resp.encoding = 'utf-8'  # 处理乱码
list_url = []

# 把源代码交给bs
main_page = BeautifulSoup(resp.text, "html.parser")
main_page2 = main_page.find('div', class_='item_list infinite_scroll', id="infinite_scroll")  # 把范围第一次缩小
alist = main_page2.find_all("a")
# print(alist)
for a in alist:
    url2 = a.get('href')  # 可以通过get拿到对应的属性的值
    url3 = 'https://www.umei.cc' + url2
    print(url3)
    # 从子页面拿到下载的路径
    child_page = BeautifulSoup(url3, "html.parser")
    p = child_page.find("div", class_='wrapper')
    img = p.find('img')
    src = img.get('src')
    # 下载图片的操作
    img_resp = requests.get(src)
    # img_resp.content 这里是以字节的形式拿到图片
    img_name = src.split('/'[-1])  # 拿到url里面最后一个/的内容
    with open('img/' + img_name, mode='wb') as f:
        f.write(img_resp.content)  # 下载文件
        print("over" + img_name)
print("all over!!!")
