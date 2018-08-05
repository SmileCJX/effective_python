#! python3
# getRowAndColumnFromExcel.py - 从表中取得行和列
import openpyxl
wb = openpyxl.load_workbook('.\\example.xlsx')
sheet = wb['Sheet1']
print(tuple(sheet['A1':'C3']))
for rowOfCellObjects in sheet['A1':'C3']:
    for cellObj in rowOfCellObjects:
        print(cellObj.coordinate,cellObj.value)
    print('---- END OF ROW ---')

sheet1 = wb.active
for cellObj in list(sheet1.columns)[1]:
    print(cellObj.value)