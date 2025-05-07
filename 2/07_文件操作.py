"""
open(文件路径,mode="",encoding=""（解码）)

文件路径：
    1.绝对路径：D:/test/xxx.text
    2.相对路径：相对于当前文件所在的文件夹
    ../  返回上一层的文件夹

mode：
    r：read  读取
    w：write 写数据
    a：append 追加写入数据
    b:读写的是非文本文件->bytes


with:上下文，不需要手动去关闭一个文件
"""
import os
import time

# f = open("1223.text", mode="r", encoding="utf-8")
# content = f.read()  # 全部读取
# print(content)
# line = f.readline().strip()  # 读一行,如果前面已经有f.read()，后面将不在按行来读取，已经读到文件末尾了
# print(line)
# line = f.readline().strip()  # 读一行
# print(line)
# line = f.readline().strip()  # 读一行
# print(line)
# content = f.readlines()  # 返回的是一个列表，每一行后面都有一个换行符
# print(content)

# 最重要的读取文件的方式：
# for line in f:#读取文件的每一行的数据
#     print(line.strip())

# 写入文件
# w模式下，如果文件不存在，自动的创建一个文件
# w模式下，每一次open都会清空掉文件中的内容
f1 = open("123455.text", mode="w", encoding="utf-8")
f1.write("胡辣汤")
f1.close()  # 尽量每次操作都要关闭文件链接

# 准备一个列表，把里面的数据写入文件里面
lst = ["12345", "2345", "1313", "13313", "133"]
f2 = open("1test.text", mode="w", encoding="utf-8")  # 大多数把打开写在文件的外面
for item in lst:
    f2.write(item + "\n")

# a模式
f3 = open("1test.text", mode="a", encoding="utf-8")
f3.write("xsk")

# with
with open("1223.text", mode="r", encoding="utf-8") as f4:
    for line in f4:
        print(line.strip())

# 文件的复制：
# 从源文件里面读取内容，然后写到新的路径里面去
# with open("1test.text",mode="r",encoding="utf-8") as f1,open("../1/1test.text",mode="w",encoding="utf-8") as f2:
#     for line in f1:
#         f2.write(line)

# with (open("1test.text", mode="r", encoding="utf-8") as f1,
#       open("../1/1test.text", mode="w", encoding="utf-8") as f2):
#     for line in f1:
#         f2.write(line)

# 修改一个文件里面的内容
# 先生成一个新的文件，把修改后的内容写道新的文件中，然后把之前的文件删掉，把新的文件重新命名为之前的文件
# 将1223.text文件里里面的数字开头从数字改为“肖”

with (open("1223.text", mode="r", encoding="utf-8") as f1,
      open("1223_副本.text", mode="w", encoding="utf-8") as f2):
    for line in f1:
        line = line.strip()
        line = "肖" + line[1:] + '\n'
        f2.write(line)

time.sleep(3)
# 删除源文件
os.remove("1223.text")
time.sleep(3)
# 把副本文件重新命名为之前的文件
os.rename("1223_副本.text", "1223.text")
