# -*- coding: utf-8 -*-
"""
Created on Fri May 22 16:27:25 2020

@author: wujinlv
Unix和Linux操作系统上提供了fork()系统调用来创建进程，
调用fork()函数的是父进程，创建出的是子进程，子进程是父进程的一个拷贝，
但是子进程拥有自己的PID。fork()函数非常特殊它会返回两次，父进程中可以
通过fork()函数的返回值得到子进程的PID，而子进程中的返回值永远都是0。
Python的os模块提供了fork()函数。由于Windows系统没有fork()调用，因此要
实现跨平台的多进程编程，可以使用multiprocessing模块的Process类来创建
子进程，而且该模块还提供了更高级的封装，例如批量启动进程的进程池（Pool）、
用于进程间通信的队列（Queue）和管道（Pipe）等。



from random import randint
from time import time,sleep
def download_task(filename):
    print('开始下载%s...'%filename)
    time_to_download=randint(5,10)
    sleep(time_to_download)
    print('%s下载完成！耗费%d秒'%(filename,time_to_download))
def main():
    start=time();
    download_task('1.pdf')
    download_task('2.avi')
    end=time()
    print('总共耗费%.2f秒'%(end-start))
if __name__=='__main__':
    main()



#多进程
from multiprocessing import Process
from os import getpid
from random import randint
from time import time,sleep

def download_task(filename):
    print('启动进程，进程号[%d].'%getpid())
    print('开始下载%s'%filename)
    time_to_download=randint(5,10)
    sleep(time_to_download)
    print('%s下载完成！耗费%d秒'%(filename,time_to_download))
def main():
    start=time()
    p1=Process(target=download_task,args=('1.pdf',))
    p1.start()
    p2=Process(target=download_task,args=('2.avi',))
    p2.start()
    p1.join()
    p2.join()
    end=time()
    print('总耗时%.2f'%(end-start))
if __name__=='__main__':
    main()
#通过Process类创建了进程对象,通过target参数我们传入一个函数来表示进程启动后要执行的代码
#后面的args是一个元组，它代表了传递给函数的参数。Process对象的start方法用来启动进程，
#而join方法表示等待进程执行结束。spyder使用的stdout和windows不支持forking，所以无法打印子进程内容。



from multiprocessing import Process
from time import sleep
counter =0
def sub_task(string):
    global counter
    while counter<10:
        print(string,end='',flush=True)
        counter+=1
        sleep(0.01)
def main():
    Process(target=sub_task,args=('ping')).start()
    Process(target=sub_task,args=('pong')).start()
if __name__=='__main__':
    main()   
#最后的结果是Ping和Pong各输出了10个
#当我们在程序中创建进程的时候，子进程复制了父进程及其所有的数据结构，
#每个子进程有自己独立的内存空间，这也就意味着两个子进程中各有一个counter变量    
"""    
    



#多个线程可以共享进程的内存空间，对“临界资源”的访问需要加上保护    
from time import sleep
from threading import Thread
class Account(object):
    def __init__(self):
        self._balance = 0
    def deposit(self, money):
        # 计算存款后的余额
        new_balance = self._balance + money
        # 模拟受理存款业务需要0.01秒的时间
        sleep(0.01)
        # 修改账户余额
        self._balance = new_balance
    @property
    def balance(self):
        return self._balance
class AddMoneyThread(Thread):
    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money
    def run(self):
        self._account.deposit(self._money)
def main():
    account = Account()
    threads = []
    # 创建100个存款的线程向同一个账户中存钱
    for _ in range(100):
        t = AddMoneyThread(account, 1)
        threads.append(t)
        t.start()
    # 等所有存款的线程都执行完毕
    for t in threads:
        t.join()
    print('账户余额为: ￥%d元' % account.balance)
if __name__ == '__main__':
    main()    
    


#通过“锁”来保护“临界资源”    
    
    
    





















