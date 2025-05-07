"""
内置函数：可以直接拿来用的函数
"""

# complex 表示复数，实部+虚部
# bin,oct,hex
a = 18  # 十进制
print(bin(a))  # 二进制 0b10010
print(oct(a))  # 八进制 0o22
print(hex(a))  # 十六进制 0x12
print(int(0b10010))  # 其它进制转换为十进制

print(pow(10, 3))  # 求a的b次方
print(10 ** 3)  # 可以有一样的效果
lst = [12, 2343456, 758, 34623, 12355, 2523, 1]
print(max(lst))  # 找列表里面的最大的数
print(min(lst))  # 找列表里面的最小的数
print(sum(lst))  # 求和
s = {1, 1, 1, 1, 23, 4, 243}
lst2 = list(s)
lst3 = list("呵呵哒")  # list里面一定有一个循环（for）
print(lst2)
print(lst3)
print(s)  # 集合里面的元素不能重复，重复的自动删除掉

# slice
s = slice(1, 4, 3)  # 这里是括号和逗号 [1:4:2]
ret = "hhhhhhhhxxxzxhshadhaohdaokl"[s]
print(ret)

# format,ord,chr
# format 格式化
print(format(18, '08b'))  # 格式化为二进制，"08b"代表的是，希望得到一个由0补充的八位二进制
print(format(18, '0'))  # 格式化为八进制
print(format(18, 'x'))  # 格式化为十六进制
# ord，chr
a = "中"  # python中使用的是unicode
print(ord(a))  # 中字在unicode里面的码位是20013
print(chr(20013))  # 给出编码位置，展现出文字
# for i in range(65536):
#     print(chr(i)+" ",end="")

# frozenset冻结的集合，不可变的集合，不能进行增删改查的集合

# enumerate,all,any
print(all([1, "", "都是把"]))  # 把all当成and来看，t and t and t
print(all([0, "", "都是把"]))  # 把all当成and来看，t and t and t
print(any([0, "", "都是把"]))  # 把any当成or来看，t or t or t
lst = ["孝顺看", "肖申克", "孝顺康", "肖顺康"]
for item in enumerate(lst):  # 可以拿到索引和元素，可以很方便地去更改列表的元素的信息
    print(item)
for index, item in enumerate(lst):  # 拿到的是一个元组
    print(index, item)
for i in range(len(lst)):  # 与enumerate的作用差不多
    print(i, lst[i])

# hash
s = "呵呵哒"
print(hash(s))  # 算出来的是一个数字，然后转换成一个内存地址，然后进行数据的存储，字典（集合）哈希表
# id
print(id(s))  # 直接得到计算的内存地址
print(dir(s))  # 可以看到对当前数据可以执行的操作