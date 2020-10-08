import os
#文件写入
with open(file="test1.txt",mode='w',encoding='utf-8') as f:
    for i in range(10):
        line = 'test1%d\n'%i
        f.write(line)

#文件复制（读取和写入）
with open(file="test1.txt",mode='r',encoding='utf-8') as f:
    with open(file="test2.txt",mode='w',encoding='utf-8') as w:
        for line in f.readlines():
            print(line)
            w.write(line.strip())



# os.remove('test1.txt')
# os.remove('test2.txt')
