from PyPDF2 import PdfReader

reader = PdfReader("example.pdf")
page = reader.pages[0]
print(reader.read_next_end_line())
#print(page.extract_text())
