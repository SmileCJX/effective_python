#! python3
# combinePdfs.py - 从多个pdf中合并选择的页面
import PyPDF2,os
# Get all the PDF filenames.
pdfFiles = []
for filename in os.listdir('.\\combine'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)
pdfFiles.sort(key=str.lower)
pdfWriter = PyPDF2.PdfFileWriter()

# Loop through all the pdf files.
for filename in pdfFiles:
    pdfFileObj = open(filename,'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    # Loop through all the pages (except the first) and add them.
    for pagenum in range(1,pdfReader.getNumPages()):
        pageObj = pdfReader.getPage(pagenum)
        pdfWriter.addPage(pageObj)

# Save the resulting PDF to a file
pdfOutput = open('.\\allminutes.pdf','wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()
