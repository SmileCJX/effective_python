#! python3
# csvDemo2.py - delimiter 和 lineterminator关键字参数
import csv
csvFile = open('.\\example.csv','w',newline='')
csvWriter = csv.writer(csvFile,delimiter='\t',lineterminator='\n\n')
csvWriter.writerow(['apples','oranges','grapes'])
csvWriter.writerow(['eggs','bacon','ham'])
csvWriter.writerow(['spam','spam','spam','spam','spam','spam'])
csvFile.close()