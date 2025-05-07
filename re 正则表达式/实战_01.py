import requests
import re
import csv

url = 'https://movie.douban.com/top250'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0'
}
resp = requests.get(url, headers=headers)
"""with open('豆瓣网页TOP250.html',mode='w',encoding='utf8') as f:
    f.write(resp.text)
print("完成")"""
page_content = resp.text

# 解析数据
obj = re.compile(r' <li>.*?<span class="title">(?P<name>.*?)'
                 r'</span>.*?<p class="">.*?<br>(?P<year>.*?)&nbsp'
                 r'.*?<span class="rating_num" property="v:average">(?P<gobal>.*?)</span>'
                 r'.*?<span>(?P<num>.*?)人评价</span>', re.S)
iter = obj.finditer(page_content)
f = open('data.csv', mode='w')
csvwriter = csv.writer(f)
for i in iter:
    dic = i.groupdict()
    dic['year'] = dic['year'].strip()
    csvwriter.writerow(dic.values())
    print(i.group('name')+' '+i.group('year').strip()+' '+i.group('gobal')+' '+i.group('num')+'人评价')
f.close()
