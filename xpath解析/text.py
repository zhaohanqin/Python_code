from lxml import etree
import requests

url = 'https://haowallpaper.com/'
headers = {
    'cookie': 'ar_debug=1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0'
}

resp = requests.get(url, headers=headers)

html = etree.HTML(resp.text)

# 这里的 XPath 路径可能需要调整，以匹配你实际想要抓取的内容
divs = html.xpath('/html/body/div[1]/div/main/div[3]/div/div/div[1]/div/div')

for i in divs:
    url2 = i.xpath('./div/div[1]/a//@href')
    if url2:  # 确保 href 属性存在
        print(url + url2[0])  # 拼接完整 URL 并打印
    else:
        print("No href found.")
