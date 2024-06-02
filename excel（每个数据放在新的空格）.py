# author 莫森 time:2024/3/3

import xlwings as xw

# 连接到Excel应用程序
app = xw.App(visible=True)  # 可见性设置为False，不显示Excel界面
workbook = app.books.open('D:\scientific\科研数据保存\小鼠实验\新建 XLSX 工作表.xlsx')  # 打开Excel文件
sheet1 = workbook.sheets['Sheet1']  # 选择Sheet1
sheet2 = workbook.sheets['Sheet2']  # 选择Sheet2

# c2_value = sheet1.range('C3').value  # 获取C2单元格的内容
# values = c2_value.split(' ')  # 使用空格进行分割
# # print(values)
# sheet2.range('C3').value = values[0]  # 写入C2单元格
# sheet2.range('D3').value = values[1]  # 写入D2单元格
# sheet2.range('E3').value = values[2]  # 写入E2单元格
# sheet2.range('F3').value = values[3]  # 写入F2单元格
# sheet2.range('G3').value = values[4]  # 写入G2单元格

# workbook.save()  # 保存文件
# workbook.close()  # 关闭文件
# app.quit()  # 退出Excel应用程序


# 获取指定范围内的单元格内容
values = sheet1.range('C2:C7').value
# 获取单元格的值
ls=[]
# print(values)
for i in values:
    value1 = i.split(' ')
    ls.append(value1)
sheet2.range('C2:K7').value=ls
# print(ls)
# 打印结果

# 关闭Excel文件
workbook.save()  # 保存文件
workbook.close()
app.quit()
