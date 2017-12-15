# coding=utf-8

#模块
# import 01
#
# student = Student('We',12,4)
# print(student.age)


# 作用域
#正常的函数和变量名是公开的，可以被直接引用
#以两个下划线开头，定义私有
# 以单个下划线开头表示protected类型的变量，即保护类型只能允许其本身与子类进行访问，不能用于from module from *



#文件操作

#写文件
def write_file():
    try:
        f = open('/Users/Felix/Desktop/Python3_Tutorial/test.txt','w')
        f.write('Hello,Python')
    except BaseException as e:
        print(e)
    finally:
        if f:
            write_file()

# IndentationError: expected an indented block 报错的解决方法：
# 在报错的所在行使用tab或者空格键进行缩进


#读文件

def read_file():
    try:
        f = open('/Users/Felix/Desktop/Python3_Tutorial/02.py','r')
        #print(f.read()) 一次性读取文件的全部内容
        print(f.readline()) #每次读取一行内容，返回list
    except BaseException as e:
        print(e)
    finally:
        if f:
            f.close()

    read_file()
