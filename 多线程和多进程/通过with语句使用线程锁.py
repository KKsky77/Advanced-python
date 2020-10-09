import sys
import threading

def loop():
    print("任务进行...")

t = threading.Thread(target=loop,name='任务1')
l = threading.Lock()
with l:
    # 执行任务...
    t.start()
    t.join()


#相当于
# some_lock.acquire()
# try:
#     # 执行任务..
# finally:
#     some_lock.release()
