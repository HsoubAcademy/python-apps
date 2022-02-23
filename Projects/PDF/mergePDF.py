import PyPDF2, os
from pathlib import Path

pdfFiles = []
for filename in os.listdir(Path.home() / Path('Desktop','article')):
   if filename.endswith('.pdf'):
       pdfFiles.append(filename)

pdfFiles.sort(key = str.lower)

pdfWriter = PyPDF2.PdfFileWriter()

for filename in pdfFiles:
    pdfFileObj = open(Path.home() / Path('Desktop','article',filename), 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    for pageNum in range(1, pdfReader.numPages):
             pageObj = pdfReader.getPage(pageNum)
             pdfWriter.addPage(pageObj)

pdfOutput = open(Path.home() / Path('Desktop','article','article.pdf'), 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()