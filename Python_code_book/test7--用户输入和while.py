
print('---------------用户输入 ==> input() -----------------------')
message = input('告诉我一些事，我给你打印出来：')
print(message)

print('------用户输入的是字符串----------')
print('-------使用int() 进行把字符串转为数值 ----------')
age = input('请输入年龄：')
print(age)
if int(age) >= 18:
    print('您已成年！')
else:
    print('你还未成年！')

print('--------求模运算符 ==> % (将两个数相除并返回余数，只会指出余数是多少！) -------------')

print('----------使用while循环  -------------')
num = 1
while num <= 5:
    print(num)
    num += 1

print('-------让用户选择何时退出---------------')
prompt = '输入信息：'
prompt += '\n输入 quit 结束'
mes = ''
while mes != 'quit':
    mes = input(prompt)
    print(mes)

print('---------使用标志---------')
prompt = '\n输入信息：'
prompt += '\n输入 quit 结束!'
act = True
mes = ''
while act:
    mes = input(prompt)
    if mes == 'quit':
        act = False
    else:
        print(mes)

print('----------使用break退出循环；把上面的例子的act = False 换成 break 即可---------------')

print('------在循环中使用continue，用法和php一样---------')

print('--------在列表之间移动元素---------')
print('使用 pop() 先删除最后一个列表中的元素，'
      '拿这个元素append()到新列表中'
      '当为空列表的时候跳出循环')

print('-----------删除包含特定值的所有列表元素----------')
print('==使用的是函数remove() 来删除列表中特定值==')

print('--------使用用户输入来填充字典---------')
ress = {}
# 设置一个标志，指出调查是否继续
poll_act = True
while poll_act:
    name = input('\n名字是：')
    res = input('喜欢去做什么？')
    # 将答卷存储在字典中
    ress[name] = res
    repeat = input('还有人要参与吗：（yes/no）')
    if repeat == 'no':
        poll_act = False
print('\n--调查结束，显示结果--')
for name, res in ress.items():
    print(name+'-----'+res+'.')






