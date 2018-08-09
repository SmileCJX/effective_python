#! python3
# freezePanes.py - 冻结窗格
import openpyxl
wb = openpyxl.load_workbook('.\\produceSales.xlsx')
sheet = wb.active
sheet.freeze_panes = 'A2'
wb.save('.\\freezeExample.xlsx')