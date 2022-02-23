import PyPDF2
from pathlib import Path

pdfFileObj = open(Path.home() / Path('Desktop','pdf_test.pdf'), 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

#pages number
print(pdfReader.numPages)

# read
pageObj = pdfReader.getPage(0)
print(pageObj.extractText())


pdfFileObj.close()