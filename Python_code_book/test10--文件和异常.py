print('------10、文件和异常------')

print('10.1.1:读取整个文件==========')
with open('pi_digits.txt') as file_obj:
    contents = file_obj.read()
    print(contents.rstrip())

print('问题1：函数open()  接收一个参数：要打开的文件的名称。把内容存储到as之后的变量名中；'
      '    使用方法 read()  来读取这个文件的全部内容，'
      '    并将作为一个长长的字符串存储在变量contents中；'
      '    最后，打印contents的值，就可将这个文本文件的全部内容显示出来；'
      ' 问题2：打印出来的结果多一个空行，因为在read()到达文件末尾时返回一个空字符串，'
      '       而将这个空字符串显示出来就是一个空行。'
      '    要删除末尾的空行，可在print（）中使用 rstrip() 删除字符串末尾的空白')

print('10.1.2：文件路径====')
print('--需要注意的是：linux和OS X中，是这样读取文件的：'
      '  with open("text_files/filename.txt") as file_obj:'
      '  在windows系统中，文件路径中使用反斜杠（\）而不是斜杆（/）；'
      '  with open("text_files\filename.txt") as file_obj:')

print('可以使用相对位置，也可以用绝对位置，注意使用的 斜杠 问题')

print('10.1.3逐行读取====')
print('逐行读取：即加个for循环读取每一行；eg:')

filename = 'pi_digits.txt'
with open(filename) as file_objs:
      for line in file_objs:
            print(line.rstrip())

print('10.1.4:创建一个包含文件各行内容的列表 ==== (相当于在with的代码块外面访问文件里的内容)')
print('使用readlines() 方法 从文件中读取每一行，并将其存储在一个列表里；')

file = 'pi_digits.txt'
with open(file) as file_obj:
      lines = file_obj.readlines()
for line in lines:
      print(line.rstrip())

print('10.1.5：使用文件的内容 ====')
print('在with外部操作文件里面的内容；')
with open(filename) as file_obj:
      lines = file_obj.readlines()
pi_string = ''
for line in lines:
      pi_string += line.strip()
print(pi_string)
print(len(pi_string))

print('10.1.6：包含一百万位的大型文件====')
# 前面的with代码块还是和上面的一样，只是打印的时候会只打印一点数据
print(pi_string[:10]+"...")
print(len(pi_string))
print('对于可处理的数据量，python没有任何限制，只要系统的内存足够多，想处理多少数据都可以。')




