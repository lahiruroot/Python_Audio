import pyttsx3
import pyPDF1
book = open('ttsl.pdf','rb')
pdfReader = pyPDF1.pdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.int()
for num in pages:
    page = pdfReader.getPage(8, pages)
    text = page.extractText()
    speaker.speek(text)
    speaker.runAndwait()
