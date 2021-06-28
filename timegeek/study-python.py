# 异常处理

# try:
#     year = int(input('input year:'))
# except Exception as e:
#     print('年份要输入数字:%s'%e)


try:
    a = open('111.txt')
except Exception as e:
    print(e)
finally:
    a.close()



