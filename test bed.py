#jina ai
from decouple import config
from jina import Flow
from docarray import DocumentArray

secret = config('JINA')
f = (
    Flow()
    .add(env={'JINA_LOG_LEVEL': 'DEBUG', 'MYSECRET': secret})
    .add(env={'JINA_LOG_LEVEL': 'INFO', 'CUDA_VISIBLE_DEVICES': 1})
)
f.save_config("envflow.yml")

JINA_AUTH_TOKEN = config('JINA')



docs = DocumentArray.from_files("rabbit.pdf", recursive=True)

f = Flow().add(uses="jinahub://PDFSegmenter")

with f:
    indexed_docs = f.index(docs)

















