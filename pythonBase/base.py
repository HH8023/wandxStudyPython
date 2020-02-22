# print absolute value of an integer:  这是注释
a = -1
if a >= 0:    # 以冒号结尾时，缩进的语句视为代码块
    print(a)
else:
    print(-a)

# 缩进，按照约定俗成的管理，始终坚持使用4个空格的缩进

# 转义 1、 可以使用转移符号 \  进行转义
#   2、还可以使用 r''表示单引号内部的字符串默认不转义。（单引号也可以换成双引号）
print(r"\n''")
print('\\\n\t\\')

#  多行文本  相当于php中的 >>>EOT
print('''测试
一个多
行文本''')

# 布尔判断
age = input('请输入年龄:')
if age >= '18':
    print('成人')
else:
    print('未成年')

# 空值
# 使用None表示，不能理解为0，因为 0 是有意义的，而None是一个特殊的空值
a = None
print(a)

# 变量 （python是动态语言，定义时不需要指定变量类型）
# 变量名 必须是大小写英文，数字和_下划线组合，且不能用数字开头（跟php一样）
# 一个变量可以反复赋值，而且可以是不同类型的变量，即可以使用多次
z = 123   # z是整数
print(z)
z = 'abc'    # z变为字符串
print(z)

# 常量
print('常量')
print(10 / 3)
print(9 / 3)
print(10 // 3)
print(10 % 3)


