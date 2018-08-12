#! python3
# writeToWord.docx - 写入word文档
import docx
doc = docx.Document()
doc.add_paragraph('hello_world!')
doc.save('.\\helloworld.docx')