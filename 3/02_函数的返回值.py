"""
返回值：函数实现后会给调用方一个结果，这个结果就是返回值

关于return：
函数执行到了return，函数就会立即停止，然后返回内容，函数内的return后买你的代码就不会执行
    1.如果函数内部没有return，最后返回的是None
    2,写了return：
        1.只写了return，后买你没跟数据，此时接受到的依然是None
        2.return值，表示函数有一个返回值，外界接受该数据(用的最多)
        3.return值1，值2.......，此时函数有多个返回值，外界接收到的是一个元组
"""


def func():
    pass


def func2():
    print(123)
    return  # 会让函数停止，后续的代码不会继续执行，类似于循环里面的break
    print(1234)


def func3():
    return 1, 2, 3, 4, 5, 6


ret = func()
print(ret)  # 如果函数内部没有return，最后返回的是None
ret = func2()
ret2 = func3()
print(ret2)
