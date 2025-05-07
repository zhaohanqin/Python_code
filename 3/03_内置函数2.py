# zip

lst1 = ["xsk", "skx", "ksx", "xxx"]
lst2 = [20, 21, 22, 24]
lst3 = [123, 234, 456, 567]

result = []
for i in range(len(lst1)):
    first = lst1[i]
    second = lst2[i]
    third = lst3[i]
    result.append((first, second, third))
print(result)

result2 = zip(lst2, lst1, lst3)  # zip拿到的结果是一个可迭代的迭代器
# print(result2)
# result2.__next__()  # 与迭代器相同，是一次性的
# for item in result2:  # 与迭代器相同，是一次性的
#     print(item)
lst = list(result2)
print(lst)  # 与上述作用相同

# locals
a = 188
print(locals())  # 此时的locals在全局作用域的范围内，这时就是看到的全局作用域中的内容


def func2():
    a = 376
    print(locals())  # 此时的locals在局部作用域的范围内，这时就是看到的局部作用域中的内容


func2()

# globals
a1 = 188
print(globals())  # 此时的globals看到是全局作用域的内容


def func3():
    a = 376
    print(globals())  # 此时的locals在全局作用域的内容


func3()
