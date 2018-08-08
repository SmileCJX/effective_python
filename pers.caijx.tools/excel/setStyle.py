#! python3
# setStyle.py - 设置单元格的字体风格
import openpyxl
from openpyxl.styles import Font
wb = openpyxl.Workbook()
sheet = wb['Sheet']
italic24Font = Font(name='Times New Roman',bold=True)
sheet['A1'].font = italic24Font
sheet['A1'] = 'Bold Times Roman'

italic24Font2 = Font(size=24,italic=True)
sheet['B3'].font = italic24Font2
sheet['B3'] = '24 pt Itaic'
wb.save('.\\styled.xlsx')