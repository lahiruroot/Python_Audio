import pyttsx3
import pyPDF1
book = open('tec.pdf','rb')
pdfReader = pyPDF2.pdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.int()
for num in pages:
    page = pdfReader.getPage(7, pages)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndwait()
