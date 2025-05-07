from threading import Thread


# 采用继承类的方式来实现线程的启动

class MyThread(Thread):
    def run(self):  # 重写父类里面的方法，这个方法是固定的，当线程被执行的时候，被执行的默认就是run方法
        for i in range(1000):
            print("子线程", i)


if __name__ == '__main__':
    t = MyThread()  # 创建一个实列
    t.start()  # 注意，这里不能用t.run那样就是方法的调用了，是单线程，t.start才是开启线程
    for i in range(1000):
        print("主线程", i)
