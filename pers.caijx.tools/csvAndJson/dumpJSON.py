#! python3
# dumpJSON.py - 用dump函数写出JSON
import json
pythonValue = {'isCat':True,'miceCaught':0,'name':'Zophie','felineIQ':None}
stringOfJsonData = json.dumps(pythonValue)
print(stringOfJsonData)