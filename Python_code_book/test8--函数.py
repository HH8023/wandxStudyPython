print('---------------定义函数 ==> def funName():-------------------')

def greet_user():
    print('hello')
greet_user()
print('---------------向函数传递信息 -------------------')
def user(name):
    print('hello '+name.title())
user('bob')

print('----------------传递实参-----------')
print('------位置实参:和php一样的用法--------')
print('注意：再使用默认值时，再形参列表中必须先列出没有默认值的形参，再列出有默认值的形参，'
      '这让python依然能够正确地解读位置实参。')


print('----返回值----')
print('函数并非总是直接显示输出，相反，它可以处理一些数据，并返回一个或一组值。'
      '函数返回的值被称为-->返回值。再函数中，可使用return 语句将只返回到调用函数的代码行。'
      '返回值让你能够将程序的大部分繁重工作移到函数中完成，从而简化主程序。')

print('--------传递列表------------')
print('-- 向函数传递列表很有用，这种列表包含的可能是名字、数字或更复杂的对象（如字典）'
      '将列表传递给函数后，函数就能直接访问内容。')

print('-----再函数中修改列表-----')
print('将列表传递给函数后，函数就可对其进行修改，在函数中对整个列表所做的任何'
      '修改都是永久性的，这让你能够高效地处理大量的数据！')

print('-----禁止函数修改列表-----')
print('有时候，需要禁止函数修改列表====> 使用切片表示法 [:] 创建列表的副本--------')

print('------------------传递任意数量的实参------------------')
print('形参名 *top 的星号让python创建一个名为top的空元组，并将收到的所有值都封装到这个元组里。')
def make_pizza(*top):
    print(top)
make_pizza('pepper')
make_pizza('mushrooms','green pep','extra cheese')
print('------结合使用位置实参和任意数量实参-----------')
print('如果要让函数接受不同类型的实参，必须在函数定义中将接纳任意数量实参的形参放在最后。'
      'python先匹配位置实参和关键字实参，再将余下的实参都收集到最后一个形参中。下面例子：')
def make_pi(size, *topp):
    print("\nMakeing a "+ str(size) + " pizza with the following toppings:")
    for top in topp:
        print("- "+top)
make_pi(19,'pep')
make_pi(20, 'mus','gree','ext')

print('----使用任意数量的关键字实参------')
print(' 有时候，需要接受任意数量的实参，但不知道传递给函数的会是什么信息，'
      '可将函数编写成能够接收任意数量的键值对----调用语句提供多少就接受多少；例子如下：')
def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('albert','einstein',location = 'princeton', field = 'physics')
print(user_profile)

print('----将函数存储再模块中-------')
print('函数的优点之一是：使用他们可将代码块与主程序分离。通过给函数指定描述性名称，可让主程序容易理解'
      '还可以将函数存储在被称为模块的独立文件中，再将模块导入到主程序中；'
      'import语句允许在当前运行的程序文件中使用模块中的代码。')
print('----导入整个模块-----')
print('查看同级目录的 pizza.py 和 如下代码')
import pizza
pizza.make_pizza(19, 'pep')
pizza.make_pizza(20,'ddd','dddff','gggg')
print('这是一种导入方法：只需编写一条import语句并在其指定模块名，就可以在程序中使用该模块的所有函数。')


print('----导入特定的函数----------')
print('语法如下： from module_name import function_name'
      'eg: from pizza import make_pizza   之后就接着调用函数即可')
from pizza import make_pizza
make_pizza(12, 'pe1p')
make_pizza(33,'dd2d','ddd3ff','gg4gg')

print('-------使用as给函数指定别名----------')
print('form pizza import make_pizza as mp'
      '上一行的mp即为给函数的别名，使用的时候也是用别名。')
print('------使用as给模块指定别名-----')
print(' import module_name as m'
      '使用时，是 m.fun_name()')

print('------导入模块中的所有函数----------')
print('from module_name import *'
      '* 号即为所有函数，使用时，也是直接写函数名即可，不需要前面加模块名')

print('在写函数时，应给函数指定描述性名称，只在其中使用小写字母和下划线。描述性可以帮助明白代码想要做什么。')

print('在给形参指定默认值时，等号两边不要有空格；函数调用时，等号两边也不要空格')



