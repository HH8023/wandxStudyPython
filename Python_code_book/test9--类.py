print('-------类的创建--------')
print('====类开始=====')
print('====注意：类的首字母大写====='
      '类的函数称为方法，self必不可少；还必须位于其他形参的前面；'
      '这是一个指向实例本身的引用，让实例能够访问类中的属性和方法')
class Dog():
    """ 一次模拟小狗的简单尝试"""
    def __init__(self, name, age):
        """ 初始化属性name 和 age"""
        self.name = name
        self.age = age
    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + " rolled over")

print('====类结束=====')

my_dog = Dog('willie', 7)
print("My dog's name is "+my_dog.name.title() + ".")
my_dog.sit()   # 调用实例中的方法;

print('----------创建多个实例----------------')
my_dog1 = Dog('aaaaa', 2)
your_dog = Dog('bbbb', 3)
my_dog1.sit()
your_dog.sit()

print('--------------------使用类和实例------------------------')
print('大部分时间都将花在使用根据类创建的实例上。')








