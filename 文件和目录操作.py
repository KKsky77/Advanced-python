import os
import shutil


#创建目录 
#os.makedirs,可以递归的创建目录结构
#exist_ok=True 指定了，如果某个要创建的目录已经存在，也不报错
os.makedirs('tmp/python',exist_ok=True)

#创建文件
with open(file='tmp/python/text3.txt',mode='w',encoding='utf-8') as f:
    f.write("测试")

#复制文件
shutil.copyfile('tmp/python/text3.txt','tmp/python/text3-dopy.txt')

#删除目录
#os.remove 可以删除一个文件
#shuti.rmtree 删除整个目录
os.remove('tmp/python/text3.txt')
if os.path.exists('tmp-copy'):
    shutil.rmtree('tmp-copy')

#拷贝目录,目标目录必须不存在
shutil.copytree('tmp','tmp-copy')


#修改文件名、目录名
try:
    os.rename('tmp/python','tmp/python1')
    os.rename('tmp/python1/text3-dopy.txt','tmp/python1/text3-dopy1.txt')
except FileExistsError as e:
    print("报错",e)

# # 目标目录
# targetDir = 'tmp'
# files = []
# dirs  = []
# fpaths = []

# # 下面的三个变量 dirpath, dirnames, filenames
# # dirpath 代表当前遍历到的目录名
# # dirnames 是列表对象，存放当前dirpath中的所有子目录名
# # filenames 是列表对象，存放当前dirpath中的所有文件名

# for (dirpath, dirnames, filenames) in os.walk(targetDir):
#     files += filenames
#     dirs += dirnames
#     for fn in filenames:
#          # 把 dirpath 和 每个文件名拼接起来 就是全路径
#         fpath = os.path.join(dirpath, fn)
#         fpaths.append(fpath)

# print(files)
# print(dirs)
# print(fpaths)


# 目标目录
#listdir返回的是该目录下面所有的文件和子目录。
targetDir = 'tmp'

# 所有的文件
print([f for f in os.listdir(targetDir) if os.path.isfile(os.path.join(targetDir, f))])

# 所有的目录
print([f for f in os.listdir(targetDir) if os.path.isdir(os.path.join(targetDir, f))])


# try:
#     shutil.rmtree('tmp-copy')
#     shutil.rmtree('tmp')
# except:
#     print("报错2")
