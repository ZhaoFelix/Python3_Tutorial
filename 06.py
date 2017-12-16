# coding=utf-8

#列表

#普通列表
list = ['test','test2','test3']
for i in list:
    print(i)

#混合列表 列表中的元素类型是不唯一的
mixList = ['test',1,'23']
for j in mixList:
    print(j)

#空列表
emptyList = []
emptyList.append('Felix') #列表元素添加,只允许添加一个元素
emptyList.extend(['Felix','添加两个元素'])#添加的是一个列表
print(emptyList)
emptyList.insert(1,'将位置添加到第二个位置')
