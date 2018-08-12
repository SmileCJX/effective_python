#! python3
# readDocx.py - 从.docx文本中取得完整的文本
import docx
def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)

print(getText('.\\demo.docx'))