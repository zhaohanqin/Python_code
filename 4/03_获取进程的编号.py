from multiprocessing import Process
from time import sleep
import os


# 创建多进程的方法与创建多线程的方法相同

def func1(num,time):
    print("获取func1的进程的pid：",os.getpid())
    print("获取父进程的pid：",os.getppid())
    for i in range(num):
        print("子进程1", i)
        sleep(time)

def func2(num):
    print("获取func2的进程的pid：",os.getpid())
    print("获取父进程的pid：",os.getppid())
    for i in range(num):
        print("子进程2", i)
        sleep(0.3)


if __name__ == '__main__':
    print("获取主线程的pid:",os.getpid())
    p1 = Process(target=func1,args=(3,0.1))
    p2 = Process(target=func2,kwargs={"num":2})

    p2.start()
    p1.start()