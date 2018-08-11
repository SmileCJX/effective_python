#! python3
# pdfDemo.py - 从pdf提取文本
import PyPDF2
pdfFileObj = open('.\\meetingminutes.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print(pdfReader.numPages)
pageObj = pdfReader.getPage(0)
print(pageObj.extractText())