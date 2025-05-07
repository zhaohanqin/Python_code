from multiprocessing import Process
from time import sleep


# 创建多进程的方法与创建多线程的方法相同

def func1():
    for i in range(10):
        print("子进程1", i)
        sleep(0.2)

def func2():
    for i in range(10):
        print("子进程2", i)
        sleep(0.3)


if __name__ == '__main__':
    #使用进程类创建对象，
    # target：指定进程执行的函数名
    # args：使用元组的方式给指定的任务传参
    # kwargs：使用字典的方式给指定任务传参
    p1 = Process(target=func1)
    p1.start()
    p2 = Process(target=func2)
    p2.start()
    for i in range(10):
        if i == 500:
            p1.join()  # 当i等于500时，主进程被阻塞，当子进程执行完以后再执行主进程
        print("主进程", i)