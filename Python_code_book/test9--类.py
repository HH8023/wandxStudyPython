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
print('大部分时间都将花在使用根据类创建的实例上。需要执行的一个重要任务是修改实例的属性。'
      '你可以直接修改实例的属性，也可以编写方法以特定的方式进行修改。')

print('汽车类')
class Car():
    """
    一次模拟汽车的简单尝试
    """
    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
    def get_des_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year)+' '+self.make+' '+self.model
        return long_name.title()
my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_des_name())

print('---给属性指定默认值----')

class Car1():
    """
    一次模拟汽车的简单尝试
    """
    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_des_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year)+' '+self.make+' '+self.model
        return long_name.title()
    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("this car has "+ str(self.odometer_reading)+ " miles on it.")
my_new_car1 = Car1('audi', 'a4', 2019)
print(my_new_car1.get_des_name())
my_new_car1.read_odometer()

print('----修改属性的值----'
      '以三种不同的方式修改属性的值：1、直接通过实例修改；2、通过方法进行设置；3、通过方法进行递增（增加特定的值）')
print('--1、直接修改属性的值--'
      '要修改属性的值，最简单的方式是通过实例直接访问')
print('还是用上面的class')
my_new_car2 = Car1('audi','a4',2019)
print(my_new_car2.get_des_name())
my_new_car2.odometer_reading = 23
my_new_car2.read_odometer()

print('--2、通过方法修改属性的值--'
      '如果有替你更新属性的方法，将大有裨益。这样你就无需直接访问属性，'
      '而可将值传递给一个方法，由它在内部进行更新。'
      '通俗来说，就是定义一个方法，传参来进行修改值')

print('--3、通过方法对属性的值进行递增--'
      '递增使用的是 += 整个方式')

print('--------继承-----------'
      '编写类时，并非总是要从空白开始，如果要编写的类是另一个现成类的特殊版本，可使用继承。'
      '一个类继承另一个类时，它将自动获得另一个类的所有属性和方法；'
      '原有的类称为父类，而新类称为子类，子类继承其父类的所有属性和方法，同时还可以定义自己的属性和方法')

print('----子类的方法  __init__  ----'
      '创建子类的实例时，python首先需要完成的任务时给父类的所有属性赋值。'
      '为此，子类的方法__init__() 需要父类施以援手。')
print('1、创建子类时，父类必须包含在当前文件中，且位于子类前面'
      '2、定义子类时，必须在括号内指定父类的名称。'
      '3、super()时一个特殊的函数，帮助python将父类和子类关联起来，'
      '父类也成为超类')
class Car11():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_desc_name(self):
        long_name = str(self.year)+' '+self.make+' '+self.model
        return long_name.title
    def read_odometer(self):
        print("This car has "+str(self.odometer_reading)+" miles on it.")
    def update_odometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
            return self.odometer_reading
        else:
            print("you cannot roll back an odometer!")
    def increment_odometer(self,miles):
        self.odometer_reading += miles
        return  self.odometer_reading
class ElectricCar(Car11):
    def __init__(self,make,model,year):
        # super(ElectricCar, self).__init__(make,model,year)
        super().__init__(make,model,year)
my_tesla = ElectricCar('tesla', 'models',2019)
print(my_tesla.update_odometer(20))

print('-----给子类定义属性和方法-------')
print('跟父类添加属性和方法一样。即在super()下面接着使用self.xxx = xxx 来定义')

print('----重写父类的方法-------')
print('在子类中定义一个与父类同名的方法，即可重写父类的方法。')

print('--将实例用作属性--')
class Car22():
    '''
    --snip--
    '''
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
    def get_desc_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name
class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size
    def describe_battery(self):
        print("打印一条描述电瓶容量的消息")
class ElectricCar(Car22):
    def __init__(self, make, model, year):
        '''
        :param make:
        :param model:
        :param year:
        '''
        super().__init__(make,model,year)
        self.battery = Battery()
my_tesla1 = ElectricCar('tesla','model s', 2016)
print(my_tesla1.get_desc_name())
my_tesla1.battery.describe_battery()

print('9.4导入类')
print('--导入单个类--')
print('使用 from 文件名 import 类名：')
print('--可以在一个文件里存储多个类，这些类之间可能是继承关系--')
print('从一个模块中导入多个类：-- from 文件名 import 类名1，类名2，...-- ；可使用 * 号代表全部类名')

print('导入整个模块：')
print('直接使用 import 文件名  导入整个文件，在文件里再使用 . 类名来创建实例')










