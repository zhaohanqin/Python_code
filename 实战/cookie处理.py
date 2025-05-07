import requests

# 登录，然后得到cookie
# 然后带着cookie去请求到书架的url，即书架上面的内容

# 连接上面的两个操作
# 我们可以使用session进行请求-> session你可以认为是一连串的请求，并且在这个过程中的cookie不会丢失

# 会话
session = requests.session()

data = {
    "loginName": '18614075987',
    "password": 'g6035945'
}
# 1.登录，目的是拿到cookie
url = 'https://passport.17k.com/ck/user/login'
session.post(url, data=data)
# print(resp.text)
# print(resp.cookies)

# 2.拿书架上的数据
# 3.因为是用session进行数据拿取，所以现在的session里面是友刚才拿取到的cookie的
resq = session.get('https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919')
print(resq.json())

# 还可以不用session,直接从网页里面拿到登录用到的cookie，包含在request的header参数里面就行
