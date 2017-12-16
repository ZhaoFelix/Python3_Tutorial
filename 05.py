# coding=utf-8

score = int(input('请输入一个分数'))
if 100>=score>=90:
    print('A')
else:
    if 90>=score>=80:
        print('B')


#三元操作符
x = 10
y = 3
small = x if x<y else y #条件成立为x,不成立则为y
print(small)


# 断言 assert 经常用于调试程序，只有当程序满足断言后的条件时，程序才能接着往下运行

for i in range(1,10,2):
    print(i)
    
