import PyPDF2

mypdf = open("1.pdf", "rb")
myread = PyPDF2.PdfFileReader(mypdf)

print("No of pages: " + str(myread.numPages))
print(myread.getPage(1))