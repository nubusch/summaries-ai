
import PyPDF2
import textract
from PyPDF2 import PdfReader

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

filename = 'rabbit.pdf'

pdfobj = open(filename, 'rb')
pdf = PyPDF2.PdfReader(pdfobj)

num_pages = PdfReader.numPages
count = 0
text = ""

while count < num_pages:
    pageobj = pdfReader.getPage(count)
    count += 1
    text += pageobj.extractText()

if  text != "":
    text = text

else:
    text = textract.process(fileurl, method="tesseract", language="eng")


tokens = word_tokenize(text)

punctuations = ['(',')',';',':','[',']',',']

stop_words = stopwords.words('english')

keywords = [word for word in tokens if not word in stop_words and not word in punctuations]


#image

import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

print(pytesseract.image_to_string('page.jpg'))




#more pdf
import re
import textract
from pandas.io import clipboard

#read the content of pdf as text
text = textract.process('rabbit.pdf')


import oneai
from decouple import config

oneai_api_key = config('ONE_AI')

pipeline = oneai.Pipeline(steps=[oneai.skills.Summarize()],)

output = pipeline.run(text)

print(output.summary.text)




#jina ai
from decouple import config
from jina import Flow
import os

secret = config('JINA')
f = (
    Flow()
    .add(env={'JINA_LOG_LEVEL': 'DEBUG', 'MYSECRET': secret})
    .add(env={'JINA_LOG_LEVEL': 'INFO', 'CUDA_VISIBLE_DEVICES': 1})
)
f.save_config("envflow.yml")

JINA_AUTH_TOKEN = config('JINA')


