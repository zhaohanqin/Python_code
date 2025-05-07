from lxml import etree
import requests

url = 'http://glidedsky.com/level/web/crawler-basic-1'

resp = requests.get(url)
html = etree.HTML(resp.text)
divs = html.xpath('/html/body/div/main/div[1]/div/div/div/div')
for i in divs:
    num = i.xpath('./div/text()')
    print(num)
