#! python3
# writeToCSV.py - Writer对象
import csv
outputFile = open('.\\output.csv','w',newline='')
outputWriter = csv.writer(outputFile)
outputWriter.writerow(['spam','eggs','bacon','ham'])
outputWriter.writerow(['Helo,world!','eggs','bacon','ham'])
outputWriter.writerow([1,2,3.1415926,4])
outputFile.close()