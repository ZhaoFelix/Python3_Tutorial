# coding=utf-8

# 元组
tuple = (1,2,4,5,67,8)
#元组的访问与列表的访问方式一样
print(tuple[:5])#切片
#元组的内容不能修改
tuple2 = 1,2,4,5 #元组
print(type(tuple2))
#创建空的元组
emptyTuple = ()
#元组与列表的区别在于,号


#元组的更新与删除

tumple3 = ('Felix','Felix2','Felix3')
#在位置2处插入一个新的元素
tumple3 =  tumple3[:1] +('Felix4',)+tumple3[1:]#元组的合并
print(tumple3)
 
