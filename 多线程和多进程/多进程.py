from multiprocessing import Process
from multiprocessing import Array

def func(i,temp):
    temp[0] += 100
    print("进程%s " % i, ' 修改数组第一个元素后----->', temp[0])

if __name__ == '__main__':
    temp = Array('i', [1, 2, 3, 4])
    for i in range(10):
        p = Process(target=func, args=(i, temp))
        p.start()