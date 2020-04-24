print('----------使用字典==》相当于php对象----------------')
alien = {'color': 'green', 'points': 5}
new_point = alien['points']
print('you just earned '+ str(new_point) + ' points!   使用str()进行转成字符串，格式要统一')

print('------------添加键值对------------')
alien['x'] = 0
alien['y'] = 24
print(alien)

print('------------删除键值对==> del alien[''] --------------')
print(alien)
del alien['points']
print(alien)

print('-------遍历所有的键值对 格式： for k, v in data.items():     items()是关键---------')
user0 = {
    'username': 'bob',
    'first': 'enrico',
    'last': 'fermi',
}
for key, val in user0.items():
    print("\nKey:" + key)
    print("\nval:" + val)

print('----------遍历字典中的所有键==> for name in data.keys():  keys()是关键--------'
      '--------遍历字典时，会默认遍历所有的键，所有 keys()是可以省略的')
fav_lang = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'c++',
}
for name in fav_lang.keys():
    print(name.title())

print('----------按顺序遍历字典中的所有键==> 使用sorted() ----------------')
print(fav_lang)
for name in sorted(fav_lang.keys()):
    print(name.title() + " thank you.......")

print('---------遍历字典中的所有值 格式：for val in data.values():  主要是values()----------------')
print(fav_lang)
for lang in fav_lang.values():
    print(lang.title())

print('------------使用 set() 找出列表中独一无二的元素---------------')

print('-----嵌套-------')
print('----------字典列表---------')
ali0 = {'color': 'green', 'points': 4}
ali1 = {'color': 'green', 'points': 4}
ali2 = {'color': 'green', 'points': 4}
ali3 = [ali0,ali1,ali2]
print(ali3)
for al in ali3:
    print(al)
print('---------使用range() 生成30个')
alien11 = []
for ali_num in range(30):  # 循环30个
    newAlien = {'color': 'green', 'points': 4}
    alien11.append(newAlien)   #给列表添加字典；
print(len(alien11))   #  打印长度
for val in alien11[:5]:   # 打印出列表的前5个
    print(val)
print('...')


