#! python3
# removeCsvHeader.py - 循环遍历每个CSV文件
import csv,os
os.makedirs('headerRemoved',exist_ok=True)

# Look through every file in the current working directory.
for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        continue # skip non-csv files

    print('Removing header from ' + csvFilename + '...')

    # Read the CSV file in (skiping first row).

    # write out the CSV file.
