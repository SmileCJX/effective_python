#! python3
# removeCsvHeader.py - 循环遍历每个CSV文件
import csv,os
os.makedirs('headerRemoved',exist_ok=True)

# Look through every file in the current working directory.
for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        continue # skip non-csv files
        csvRows = []
        csvFileObj = open(csvFilename)
        readerObj = csv.reader(csvFileObj)
        for row in readerObj:
            if readerObj.line_num == 1:
                continue # skip first row
            csvRows.append(row)
        csvFileObj.close()
    print('Removing header from ' + csvFilename + '...')

    # write out the CSV file.
