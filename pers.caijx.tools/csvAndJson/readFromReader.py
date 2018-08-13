#! python3
# readFromReader.py - 在for循环中，从Reader对象读取数据
import csv
exampleFile = open('.\\example.csv')
exampelReader = csv.reader(exampleFile)
for row in exampelReader:
    print('Row #' + str(exampelReader.line_num) + ' ' + str(row))