# 原理：通过第三方的机器去发送请求

import requests

# 113.223.212.207:8089
# 117.71.149.97:8089
# 42.63.65.43:80
# 113.124.86.253:9999
proxies = {
    'https': 'https://113.124.86.253:9999'
}

url = 'https://www.baidu.com'
resp = requests.get(url, proxies=proxies)
resp.encoding = 'utf-8'
print(resp.text)
