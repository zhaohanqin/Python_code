import io
import sys
from bs4 import BeautifulSoup
import requests

# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #�ı��׼�����Ĭ�ϱ���

# ���� http://www.XXX.com/example.html
url = 'http://www.XXX.com/example.html'
page = requests.get(url)
page.encoding = 'utf-8'
data = BeautifulSoup(page.text, 'lxml')
print(data)
