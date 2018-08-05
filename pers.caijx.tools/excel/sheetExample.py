#! python3
# sheetExample.py - 从工作簿中取得工作表
import openpyxl
wb = openpyxl.load_workbook('.\\example.xlsx')
print(str(wb.sheetnames))
sheet = wb['Sheet3']
print(str(sheet))
print(type(sheet))
print(sheet.title)
anotherSheet = wb.active
print(str(anotherSheet))