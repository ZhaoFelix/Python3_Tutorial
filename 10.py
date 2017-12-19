# coding=utf-8

#函数文档

def sayName(name):
    '函数的文档内容'
    print(name)

#查看参数的文档
print(sayName.__doc__)



#内嵌函数和闭包
count = 5
def myFun():
    count = 10
    print(10)

myFun()#调用该函数不会修改count的值，需要修改count的值时需要在函数的局部变量前添加global关键字
print(count)


#内嵌函数


def fun1():
    print('调用函数一')
    def fun2():
        print('调用函数二')
    fun2()
#内嵌函数不能被外部调用
fun1()

#闭包
def funx(x):
    def funY(y):
        return x*y
    return funY
i = funx(5)(8)
print(i)
