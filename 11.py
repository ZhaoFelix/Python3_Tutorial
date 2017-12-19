# coding=utf-8


#lambda表达式

def ds(s):
    return 2*s+1

#lambda实现相同的函数功能
#  a = lambda x:2*x+1
# print(a)

#lambda表达式简化了函数的定义过程

#输出1到100的偶数
start = 1
while True:
    if start==51:
        break
    print(start*2)
    start += 1

print('-------------------------')

#输出1到100的奇数
end = int(input('请输入计算的范围:'))
prior  = 1;
while True:
    if prior==100:
        break
    if prior%2==1:
        print(prior)
    prior += 1

print('-------------------------')

#计算1-2+3-4+5-6+..+99-100的和
sum = 0
symbol =  1

while True:
    if symbol==end+1:
        break

    if symbol%2 == 1:
        sum = sum  + symbol
    if start%2 == 0:
        sum = sum - symbol
    symbol += 1
print sum;
