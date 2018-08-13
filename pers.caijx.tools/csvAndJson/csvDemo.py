#! python3
# csvDemo.py - 从CSV中读取数据
import csv
exampleFile = open('.\\example.csv')
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)
print(exampleData)
print(exampleData[0][0])
print(exampleData[0][1])
print(exampleData[0][2])
print(exampleData[1][1])
print(exampleData[6][1])