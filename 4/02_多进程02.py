from multiprocessing import Process
from time import sleep


# 创建多进程的方法与创建多线程的方法相同

def func1(num,time):
    for i in range(num):
        print("子进程1", i)
        sleep(time)

def func2(num):
    for i in range(num):
        print("子进程2", i)
        sleep(0.3)


if __name__ == '__main__':
    #使用进程类创建对象，
    # target：指定进程执行的函数名
    # args：使用元组的方式给指定的任务传参
    # kwargs：使用字典的方式给指定任务传参
    p1 = Process(target=func1,args=(3,2))
    p1.start()
    p2 = Process(target=func2,kwargs={"num":2})
    p2.start()