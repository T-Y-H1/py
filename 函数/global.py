# gloabal语句
# 使用 global 语句可以给在函数外定义的变量赋值

x = 50

def func():
    global x
    print("x is ",x)
    x = 3
    print("change global x to ",x)

func()
print("x is",x)