import re

s = "15100649928,123@qq.com,+8613653287791,666@163.com"
ret=re.findall(r"(?:\+86)*1[3-9]\d{9}",s)
print(ret)