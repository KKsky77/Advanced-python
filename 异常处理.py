# try:
#     可能产生异常的代码块
# except [ (Error1, Error2, ... ) [as e] ]:
#     处理异常的代码块1
# except [ (Error3, Error4, ... ) [as e] ]:
#     处理异常的代码块2
# except  [Exception]:
#     处理其它异常
# finally：
#     最终处理
#

# try:
#     a = int(input("输入被除数："))
#     b = int(input("输入除数："))
#     c = a / b
#     print("您输入的两个数相除的结果是：", c )
# except (ValueError, ArithmeticError) as e:
#     print("Error:",e)
#     print("程序发生了数字格式异常、算术异常之一")
# except :
#     print("未知异常")
# finally:
#     print('finally 被执行了')
# print("程序继续运行")


# try:
#     raise TypeError('类型错误')
# except Exception as e:
#     print(e)

assert 1 == 2   #在此处中断

print("程序结束！")