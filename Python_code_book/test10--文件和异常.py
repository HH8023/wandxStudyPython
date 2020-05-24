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







