"""
内容回顾：
    1.函数可以作为参数进行传递
    2.函数可以作为返回值返回
    3.函数可以像变量一样进行赋值操作

装饰器：可以直接记住最后的结论
     本质上是一个闭包
     作用：不改变原有的函数的调用的情况下，给函数添加新的功能
     即：在函数前后添加新的功能，但是不改变原来的代码


     在用户登录的地方，日志等方面有很大的作用
     雏形：
     def wrapper(fn):
        def inner():
            #在目标执行之前完成的操作
            fn()
            #在目标执行后完成的操作
        return inner   #这里一定不能加上小括号


    没有返回值的情况下：
     def wrapper(fn):
        def inner(*args, **kwargs):
            #在目标执行之前完成的操作
            fn(*args, **kwargs)
            #在目标执行后完成的操作
        return inner   #这里一定不能加上小括号

"""


def guanjia(game):  # 设定一个游戏管家，让管家帮忙执行打开和关闭外挂的操作
    def inner(*args, **kwargs):  # inner添加了参数，args一定是一个元组，kwargs一定是一个字典
        print("打开外挂")
        game(*args, **kwargs)  # 这里的*和上面的*不一样，这里的表示将args和kwargs打散成位置参数和关键字参数,如果这里没有使用*和**后面打印的就是元组和字典格式
        print("关闭外挂")

    return inner


@guanjia  # 相当于play_dnf = guanjia(play_dnf)的操作
def play_dnf(username, password):
    print("12345dnf", username, password)


@guanjia  # play_lol = guanjia(play_lol)
def play_lol(username, password,hero):
    print("德玛西亚！！！！！！！！！", username, password,hero)

play_dnf("12123131","123131231")
play_lol("123124",1241412,"gailun")