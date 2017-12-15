# coding=utf-8

print ("Hello,world")
#整型变量
a = 100
#字符串
b = 'Felix'
print(a,b) #多变量输出

#字符串换行
#元祖的元素不能修改，没有append(),insert()这样的函数
'''
list []
tuple ()
dictionary {}、()
sets 无序不重复元素的序列 {}或者set()函数创建
'''

#条件控制
'''
1.每个条件后面要使用：
2.使用缩进来划分语句块，相同缩进数的语句在一起组成一个语句块
3.elif 相当于 else if
4.在Python中没有swift-case语句
'''
age = 18
if age<=2:
    print('婴儿')
elif age<=5:
    print('幼儿')
else:
    print('其他')


#循环
names = ['n1','n2','n3']
for name in names:
    print(name)

m = 5
n = 0
while n <=5 :
    n += 1
    print('循环次数:'+str(n))
else:
    print('不符合条件')
#python中没有do-while循环


# 函数
# 函数的定义使用def关键字，函数命名全部小写
def hello():
    print('Hello,world')
hello() #函数调用

def hello(x,y):
    print(x+y)
hello(1,3)

#设置默认参数
def  hello2(x,y,z=8):
    print(x+y+z)
hello2(2,3)
hello2(3,5,6)

# 可变参数
def hello3(*y): #参数前加*表示不止一个参数
    print(y)
hello3(1,2,3,45)

#关键字参数
print('----关键字参数-----')
def hello4(x,**y):
    print(x,y)
hello4(1024);
hello4(1,age = 2,name = 3.5)

#返回值
def hello5(x):
    return x

#全局变量

z = 1024
def hello6():
    global z
    z = 520
    print('z='+str(z))
hello6()
