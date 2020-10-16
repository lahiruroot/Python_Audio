import pyttsx3
import pyPDF1
book = open('ttsl.pdf','rb')//get value
pdfReader = pyPDF1.pdfFileReader(booktext)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.int()
for num in pages:
    page = pdfReader.getPage(8, pages)
    text = page.extractText()
    speaker.speek(mytext)
    speaker.runAndwait()
