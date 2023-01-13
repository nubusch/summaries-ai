import fitz

pdf = fitz.open('theory-21.pdf')
page = pdf[0]
annot = page.first_annot
print(annot.info['content'])
next_annot = annot.next
print(next_annot.info['content'])
pdf.close()


