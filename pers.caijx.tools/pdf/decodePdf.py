#! python3
#decodePdf.py - 解密pdf
import PyPDF2
pdfReader = PyPDF2.PdfFileReader('.\\encrypted.pdf','rb')
# print(pdfReader.isEncrypted)
# print(pdfReader.getPage(0))
pdfReader.decrypt('rosebud')
print(pdfReader.getPage(0))