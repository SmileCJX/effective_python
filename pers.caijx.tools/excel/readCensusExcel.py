#! python3
# readCensusExcel.py - 从人口普查电子表格文件中读取数据，并在几秒钟内计算出每个县的统计值
import openpyxl,pprint
print('Opening workbook...')
wb = openpyxl.load_workbook('.\\censuspodata.xlsx')
sheet = wb['Population by Census Tract']
countryData = {}

# Fill in countryData with each country's population and tracts.
print('Reading rows...')
for row in range(2,sheet.max_row + 1):
    # Each row in the spreadsheet has data for one census tract.
    state = sheet['B' + str(row)].value
    country = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value
