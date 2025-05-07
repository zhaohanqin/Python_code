import requests

# 登录，然后得到cookie
# 然后带着cookie去请求到书架的url，即书架上面的内容

# 连接上面的两个操作
# 我们可以使用session进行请求-> session你可以认为是一连串的请求，并且在这个过程中的cookie不会丢失

# 会话
session = requests.session()
