#  #!/usr/env/bin python3
# -*- coding:utf-8 -*-

print('-------------使用for循环打印数组  用 in ------------')
magicians = ['aaa', 'bbb', 'ccc']
for magician in magicians:
    print(magician.title() + ',表演真的很棒！')

print('-------------使用函数range() 第一个参数为开始数，第二个为指定的值停止（不包含第二个值） ------------------')
for val in range(1, 9):
    print(val)

print('------------使用range() 指定步长（第三个参数）-------')
evenum = list(range(2, 11, 2))
print(evenum)

print('-------------使用range() 创建数字列表-------------')
num = list(range(1, 5))
print(num)

print('例子：创建一个列表，其中包含前10个整数（1-10）的平方？')
squ = []
for val in range(1, 11):
    sq = val ** 2
    squ.append(sq)
print(squ)
print('找出squ的最大，最小，总和的值')
print('最大：')
print(max(squ))
print('最小：')
print(min(squ))
print('总和：')
print(sum(squ))

print('--------------列表解析----------------------')
squares = [val ** 2 for val in range(1, 11)]
print(squares)
print('------列表解析怜惜-----------')
numlist = [val for val in range(1, 21)]
print(numlist)
sum = 0
for val in range(1, 1000001):
    sum += val
print(sum)

print('-----------奇数------------------')
jishu = [val for val in range(1, 20, 2)]
for n in jishu:
    print(n)

print('-------------3的倍数--------------')
list3 = []
for v in range(3, 30, 3):
    list3.append(v)
print(list3)



print("----------------------------切片---------------------------")





