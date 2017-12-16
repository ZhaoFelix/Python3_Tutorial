# coding=utf-8

#列表的操作
list1 = [123]
list2 = [321]
list3 = [543]

list4 = list3 + list2 + list1 #列表拼接
print(list4)

list5 = list4 * 3
isIn = 3453  in list5 #判断某个元素是否在某个列表中
print(isIn)

#终端运行 dir(list)打印出与列表相关的函数

list6 = list5.reverse() #列表倒置

print(list5,list6)

print(list5.sort()) #对列表进行排序
