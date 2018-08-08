#! python3
# setStyle.py - 设置单元格的字体风格
import openpyxl
from openpyxl.styles import Font
wb = openpyxl.Workbook()
sheet = wb['Sheet']
italic24Font = Font(size=24,italic=True)
sheet['A1'].font = italic24Font
sheet['A1'] = 'Hello World!'
wb.save('.\\styled.xlsx')