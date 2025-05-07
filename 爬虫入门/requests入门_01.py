import requests
from bs4 import BeautifulSoup

query=input('请输入内容')
url = f'https://www.sogou.com/web?query={query}'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0"
}
resp = requests.get(url,headers=headers)
print(resp)
resp.encoding='utf-8'
print(resp.text)

