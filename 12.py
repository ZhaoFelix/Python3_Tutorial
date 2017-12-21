#coding='utf-8'

#面向对象编程

class  Student(object):
    def __init__(self, name):
        self.name = name
# __inti__方法的第一个参数永远是self，表示创建的实例本身



#类的私有变量

class Teacher(object):
    def __init__(self, name):
        self.__name = name
    def print_name(self):
        print '%s'%(self.__name)
        
