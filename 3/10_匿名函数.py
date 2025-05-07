"""
匿名函数：
    lambda表达式
    语法：
        变量=lambda 参数，参数2，参数3.....:返回值
"""


def func(a, b):
    return a + b


ret = func(13, 12)
print(ret)

# 匿名函数：
fn = lambda a, b: a + b
print(fn)  # <function <lambda> at 0x00000180B7EC0040>fn是一个函数
print(fn(13,14))
