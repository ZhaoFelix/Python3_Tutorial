# coding=utf-8
#Python中不存在字符
str1 = 'I love Python'
#字符串的遍历
for i in str1:
    print(i)

#把字符串的首字母改为大小
str = 'i am felix'
str.capitalize()
print(str)
str2 = 'FELIX'
# print(str2.casefold())#把字符串全部改为小写
print(str.center(40))#空格填充
print(str.count('i'))#计算指定字符串在目标字符串中出现的次数
print(str.endswith('x'))#判断结尾
print(str.startswith('x'))

str3  = 'I\tlove\tyou'
print(str3.expandtabs())#将字符串中的\t转换为空格
