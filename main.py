import pyttsx3
import PyPDF2

pdf = open('Algorithmic_Puzzles.pdf', 'rb')  # loading the pdf file into pdf
pdfReader = PyPDF2.PdfFileReader(pdf)        # converting it into PyPDF format
pages = pdfReader.numPages                   # counting the number of pages and assigning it to variable pages
speaker = pyttsx3.init()                     # initializing the python text to speech speaker
for p in range(26, pages):                   # This will run from x to the last page
    page = pdfReader.getPage(26)             # getting the exact page into variable page
    text = page.extractText()                # extracting contents from the current page
    speaker.say(text)                        # python text to speech will raed the text
    speaker.runAndWait()                     # it will continue reading it, until we stop it