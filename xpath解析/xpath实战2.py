from lxml import etree
import requests

url = 'https://ssr1.scrape.center/'

for j in range(1, 12):
    resp = requests.get(url + "page/" + f"{j}")
    html = etree.HTML(resp.text)
    divs = html.xpath('/html/body/div/div[2]/div[1]/div[1]/div')
    for i in divs:
        name = i.xpath('./div/div/div[2]/a/h2/text()')[0]
        gobal = str(i.xpath('./div/div/div[3]/p/text()')[0]).strip()
        url2=i.xpath('./div/div/div[1]/a/@href')[0]
        print(name.split(" ")[0],end="    评分为：")
        print(gobal,end='  链接为：')
        print(url+url2)
