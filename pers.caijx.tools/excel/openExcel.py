#! python3
# openExcel.py - 用openpyxl模块打开Excel文档
import openpyxl
wb = openpyxl.load_workbook('.\\example.xlsx')
print(type(wb))