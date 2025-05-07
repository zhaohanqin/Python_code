"""
生成器表达式：(数据 for循环 if判断)->一次性的
"""

gen = (i ** 2 for i in range(10))
print(gen)  # <generator object <genexpr> at 0x000002DBA96A81E0>
# print(gen.__next__())
# print(gen.__next__())
# print(gen.__next__())
# print(gen.__next__())
# print(gen.__next__())
# print(gen.__next__())
# print(gen.__next__())

# 把迭代器放到一个列表里面
s = list(gen)  # 如果有上面的打印，就会从最后的位置开始来拿数据
print(s)
