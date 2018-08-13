#! python3
# loadJSON.py - 用load()函数读取JSON
import json
stringOfJsonData = '{"name":"Zophie","isCat":"true","miceCaught":0,"felingIQ":"null"}'
jsonDataAsPythonValue = json.loads(stringOfJsonData)
print(jsonDataAsPythonValue)