import requests

url = 'https://fanyi.baidu.com/sug'  # 百度翻译
s = input('请输入你要翻译的英文单词')
dat = {
    'kw': s
}
# 发送post请求，发送的数据必须放在字典中，通过data参数来进行传递
res = requests.post(url, data=dat)
print(res.text)
print(res.json())  # 将服务器返回的内容直接处理为json()=>dict字典
for i in range(0,len(res.json()['data'])):
    print(res.json()['data'][i]['v'])
