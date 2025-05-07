import requests

url = 'https://movie.douban.com/j/chart/top_list'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0'
}

# 重新封装参数
param = {
    'type': '24',
    'interval_id': '100:90',
    'action': '',
    'start': 0,
    'limit': 20
}
res = requests.get(url=url, params=param, headers=headers)
print(res.request.url)
print(res.request.headers)
print(res.text)
print(res.json()[2])
res.close()  # 关掉res
