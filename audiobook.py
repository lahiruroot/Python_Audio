import pyttsx3
import pyPDF2
book = open('Test12.pdf','rb') //Get value 
pdfReader = pyPDF2.pdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.int()
for num in pages:
    page = pdfReader.getPage(7, pages)
    text = page.extractText()
    speaker.say(text) //output
    speaker.runAndwait()
