from urllib.request import urlopen

url = "http://www.baidu.com"
resp = urlopen(url)
#print(resp.read().decode("utf-8"))
with open("百度.html", mode="w", encoding="utf-8") as f:
    f.write(resp.read().decode("utf-8"))  # 读取网页的页面源代码
print("完成")
