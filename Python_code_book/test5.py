print('-----------if语句----------------')
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
print('-----upper()是进行全大写的方式打印')
print('-----lower()是转换为小写')
print('检查特定值是否包含在列表中，使用关键字 in '
      '反之，检查特定值是否不包含在列表中，用关键字 not in')
requ = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requ)
print('mush' not in requ)

print('--------动手试一试')
car1 = 'subaru'
print("Is car1 == 'subaru' ? I predict Ture.")
print(car1 == 'subaru')



