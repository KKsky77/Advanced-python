import sys
import threading
import time


t00 = time.time()
# 获取当前时间戳
def cs1():
    time0 = time.time()
    for x in range(9):
        print(x + time.time()-time0)
        # 计算用了多少时间
        print(threading.current_thread().name)
        # 打印这个线程名字

def cs2():
    for x1 in range(6,9):
        print(x1)
        print(threading.current_thread().name)

threads=[]
# 定义一个空的列表
t1 = threading.Thread(target=cs1)
t2 = threading.Thread(target=cs2)
threads.append(t1)
threads.append(t2)
# 把这两个线程的任务加载到这个列表中
for x in threads:
    x.start()
    # 然后执行，这个案例很常用，就是有多个函数要多线程执行的时候用到
    # 如果一个程序有多个函数，但是你只想其中的某一个或者某两个函数多线程，用法一样加入空的列表即可
    x.join()
    #线程堵塞 先运行第一个在运行第二个
#x.join()
#注意你的join放在这里是没有意义的，和不加join一样。线程不堵塞  但是会出现不匀称的表现  并且会修改不同线程中的变量
print('use time.{}'.format(time.time()-t00))