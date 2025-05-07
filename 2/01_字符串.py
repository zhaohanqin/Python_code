# 1.字符串的格式化的问题
# %s代表字符串的占位，%d整数的占位
name = "xskxsk"
age = 12
address = "ssss"
s = "我叫%s，住在%s，年龄是%d" % (name, address, age)
s1 = "我叫{}，住在{}，年龄是{}".format(name, address, age)
s3 = f"我叫{name}，住在{address}，年龄是{age}"  # f-string
print(s1)
print(s)
print(s3)

# ==========================================================================================================================================================
# 2.索引和切片
# 索引：按照位置来提取元素
s = "我叫谁是设"
print(s[3] + s[0])
print(s[-1])  # -1表示倒数第一，-2表示倒数第二

# 切片，从字符串中切出一部分内容
print(s[2:4])  # 从索引第2开始，第四个结束，切片拿不到第二个元素的位置，右开区间，[start,end)
print(s[0:4])  # 从开始开始可以省略
print(s[0:])  # 从可以一直取到结尾
print(s[:])  # 全部的字符串
print(s[-3:-1])  # 全部的字符串，第倒数第三个到倒数第一个，(从左往右)

s = "我爱你"
# 给切片添加步长，控制切片的方向
print(s[::-1])  # 第一个代表是整个字符串，第二个冒号代表从右往左步幅为1，-代表从右往左
# 语法：s[start,end,step]，从start到end，没step出来一个元素
s = "abcdefghijklmnopq"
print(s[2:8:3])
print(s[-1:--8:-3])

# ==========================================================================================================================================================
# 3.字符串的常规的操作
# 字符串的操作一般不会对原来的字符串影响，会产生一个新的字符串
s = "python"
s1 = s.capitalize()  # 将一个单词的首字母变为大写的
print(s1)

s = "I have a dream"
s1 = s.title()  # 将一段话的首字母都变为大写
print(s1)

s = "I HAVE A DREAM"
s1 = s.lower()  # 将字符串s里面的字母都变为小写
print(s1)

s = "i have a dream"
s1 = s.upper()  # 将s里面的字母都变为大写
print(s1)
# 常用于忽略输入的验证码的大小写
# 例子：
# verify_code = "xdA1"
# user_input = input(f"请输入验证码{verify_code}")
# if verify_code.upper() == user_input.upper():
#     print("验证成功")
# else:
#     print("验证失败")

# 3.2切割和替换
# strip()去掉左右两端的空白符(空格，\n,\t)
s = "   你好   ，我叫  周杰伦    "
s1 = s.strip()
print(s1)

# 案列
# username = input("请输入用户名：").strip()
# password = input("请输入密码：").strip()
# if username == "admin":
#     if password == "123456":
#         print("登录成功")
#     else:
#         print("登录失败")
# else:
#     print("登录失败")

# replace(old,new)字符串的替换
s = "i have a dream"
s1 = s.replace(" ", "")
print(s1)

# split(用什么来切割)字符串的切割
a = "python_java_c_c#"
a1 = a.split("_")  # 用下划线来切割,切割得到的结果会放到一个列表中
print(a1)

# ==========================================================================================================================================================
# 3.3查找和替换
# 查找
s = "你好，我叫周杰伦"
ret = s.find("周杰伦")  # 返回的是查找的目标在字符串中出现的位置，返回-1则代表没有
print(ret)
ret = s.index("周杰伦")  # 返回的是查找的目标在字符串中出现的位置
print(ret)
# ret = s.index("周润发")  # 如果报错则表示没有这段字符
# print(ret) 

print("周润发" in s)
print("周润发" not in s)

# 判断
# name = input("输入你的名字：")
# if name.startswith("肖"):  # 判断字符串的开头，.endswith()判断是否以XXX结尾
#     print("你姓肖")
# else:
#     print("你不姓肖")
# .isdigit()判断字符串是否是整数组成
# .isdecimal()判断字符串是否是小数组成

# ==========================================================================================================================================================
s = "hello"
print(len(s))  # 获得字符串的长度
# join()
lst = ['赵本山', '周星驰', '王大拿', '马大哈']
s = "_".join(lst)  # 与split()相对应
s1 = "".join(lst)
print(s + s1)
