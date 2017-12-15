# coding=utf-8

# 类

class Student(object):
    #定义类属性
    name = 'Felix'
    age = 23
    #变量名两个下划线开头，定义私有属性，这样在类外部无法直接进行访问，类的私有方法也无法访问
    __sex = 0
    #定义构造方法
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.__sex = sex
    #类方法
    def get_sex(self):
        return self.__sex
    def set_sex(self,sex):
        self.__sex = sex
#调用
if __name__ == '__main__':
        student = Student('Felix',12,1) #实例化v成员变量
print(student.age,student.name)


#单继承

class TopStudent(Student):
    top_id = 1024
    def __init__(self,name,age,sex,top_id):
        #调用父类的构造方法
        super(TopStudent,self).__init__(name,age,sex)
        self.top_id = top_id
     #重写父类方法
    #  def set_sex(self,sex):
    #      self.__sex = sex+1
    #      print('重写父类的方法')

#调用
if __name__ == '__main__':
    topStudent = TopStudent('Felix1',45,0,2048)
    print(topStudent.set_sex(1))
