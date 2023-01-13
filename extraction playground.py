


import fitz
import os

filename = os.path.join(sys.path[0], "theory-21.pdf", "r")

doc = fitz.open(filename)
print(doc)





