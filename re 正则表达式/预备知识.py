# 元字符，具有固定含义的特殊符号
"""
1  . 匹配除换行符以外的任意字符
2  \\w 匹配字母或数字或下划线
3  \\s 匹配任意的空白符
4  \\d 匹配数字
5  \n 匹配一个换行符
6  \t 匹配一个制表符
7
8  ^ 匹配字符串的开始
9  $ 匹配字符串的结尾
10
11  \\W 匹配非字母或数字或下划线
12  \\D匹配非数字
13  \\S匹配非空白符
14  a|b 匹配字符a或字符b
15  () 匹配括号内的表达式，也表示一个组
16  [...] 匹配字符组中的字符
17  [^...] 匹配除了字符组中字符的所有字符
"""
# 量词，控制元字符出现的次数
"""
1  * 重复零次或更多次
2  + 重复一次或更多次
3  ? 重复零次或一次
4  {n} 重复n次
5  {n,} 重复n次或更多次
6  {n,m} 重复n到m次
"""
# 贪婪匹配和惰性匹配
"""
1 .* 贪婪匹配
2 .*? 惰性匹配
"""

import requests
import re

# findall 匹配字符串中所有符合正则的内容
list = re.findall(r"\d+", "我的电话号码是：13277657656，他的1电话号码是：123456789")
print(list)

# finditer 匹配字符串中所有的内容，返回的是迭代器，从迭代器里面拿到内容需要.group()
iter = re.finditer(r"\d+", "我的电话号码是：13277657656，他的1电话号码是：12345678901")
print(iter)
for i in iter:
    print(i)
    print(i.group())

# search 找到一个结果就返回，返回的结果是match对象，拿数据需要.group()
s = re.search(r"\d+", "我的电话号码是：13277657656，他的1电话号码是：12345678901")
print(s)
print(s.group())

# match是从头开始匹配,相当于 r"^\d+"
s = re.match(r"\d+", "13277657656，他的1电话号码是：12345678901")
print(s.group())

# 预加载正则表达式,可以反复地使用
obj = re.compile(r"\d+")
iter = obj.finditer("我的电话号码是：13277657656，他的1电话号码是：12345678901")
print(iter)
for i in iter:
    print(i.group())

# 实战
# (?P<分组名字>正则)可以单独从正则匹配的内容中进一步提取内容
s = """
    <div class='jay'><span id='1'>郭麒麟</span></div>
    <div class='jj'><span id='2'>宋铁</span></div>
    <div class='jolin'><span id='3'>大聪明</span></div>
    <div class='sylar'><span id='4'>范思哲</span></div>
    <div class='tory'><span id='5'>胡说八道</span></div>
"""
obj = re.compile(r"<div class='.*?'><span id='(?P<id>\d+)'>(?P<name>.*?)</span></div>",re.S)#re.S 让.能匹配换行符
iter = obj.finditer(s)
for i in iter:
    print(i.group('name') + i.group('id'))
