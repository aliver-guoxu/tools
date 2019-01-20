import os
import openpyxl
import time

def get_list():
    path=input('请输入文件加所在的路径：')
    name_list=os.listdir(path)
    wb=openpyxl.Workbook()
    ws=wb.active
    j=1
    for name in name_list:
        ws.cell(row=j,column=1).value=name
        j=j+1
    wb.save('name_list.xlsx')
    print('创建成功')
    time.sleep(3)

if __name__ == '__main__':
    get_list()