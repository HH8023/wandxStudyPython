#!/usr/bin/python3

import xlrd
#'znyx-costlist.xlsx'

import xlrd
from xlrd import xldate_as_tuple
import datetime

data1 = xlrd.open_workbook(r'D:\workspace\pythonwork\study-python\pytest\\znyx-cost-template.xlsx')

table = data1.sheets()[0]
table = []
def import_ecxel(excel):
    for rown in range(excel.nrown):
        array['road_name'] = table.cell_value(rown, 0)
        array['bus_plate'] = table.cell_value(rown, 1)
        if table.cell(rown, 2).ctype == 3:
            date = xldate_as_tuple(table.cell(rown, 2).value, 0)
            array['timeline'] = datetime.datetime(*date)
        array['road_type'] = table.cell_value(rown, 3)
        array['site'] = table.cell_value(rown, 4)
        tables.append(array)

if __name__ == '__main__':
    import_ecxel(table)
    for i in table:
        print(i)
# # 初始化方法
# def __init__(self, data_path, sheetname):
#     #定义一个属性接收文件路径
#     self.data_path = data_path
#     # 定义一个属性接收工作表名称
#     self.sheetname = sheetname
#     # 使用xlrd模块打开excel表读取数据
#     self.data = xlrd.open_workbook(self.data_path)
#     # 根据工作表的名称获取工作表中的内容（方式①）
#     self.table = self.data.sheet_by_name(self.sheetname)
#     # 根据工作表的索引获取工作表的内容（方式②）
#     # self.table = self.data.sheet_by_name(0)
#     # 获取第一行所有内容,如果括号中1就是第二行，这点跟列表索引类似
#     self.keys = self.table.row_values(0)
#     # 获取工作表的有效行数
#     self.rowNum = self.table.nrows
#     # 获取工作表的有效列数
#     self.colNum = self.table.ncols

# 定义一个读取excel表的方法
def readExcel(self):
    # 定义一个空列表
    datas = []
    for i in range(1, self.rowNum):
        # 定义一个空字典
        sheet_data = {}
        for j in range(self.colNum):
            # 获取单元格数据类型
            c_type = self.table.cell(i,j).ctype
            # 获取单元格数据
            c_cell = self.table.cell_value(i, j)
            if c_type == 2 and c_cell % 1 == 0:  # 如果是整形
                c_cell = int(c_cell)
            elif c_type == 3:
                # 转成datetime对象
                date = datetime.datetime(*xldate_as_tuple(c_cell,0))
                c_cell = date.strftime('%Y/%d/%m %H:%M:%S')
            elif c_type == 4:
                c_cell = True if c_cell == 1 else False
            sheet_data[self.keys[j]] = c_cell
            # 循环每一个有效的单元格，将字段与值对应存储到字典中
            # 字典的key就是excel表中每列第一行的字段
            # sheet_data[self.keys[j]] = self.table.row_values(i)[j]
        # 再将字典追加到列表中
        datas.append(sheet_data)
    # 返回从excel中获取到的数据：以列表存字典的形式返回
    return datas
if __name__ == "__main__":
    data_path = "znyx-cost-template.xlsx"
    sheetname = "Worksheet"
    get_data = ExcelData(data_path, sheetname)
    datas = get_data.readExcel()
    print(datas)




exit()