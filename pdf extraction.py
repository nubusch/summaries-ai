from docarray import DocumentArray
from jina import Flow
from decouple import config

JINA_AUTH_TOKEN=config('jina_key')


docs = DocumentArray.from_files("test_pdf_ai.pdf", recursive=True)

flow = (
    Flow()
    .add(uses="jinahub+sandbox://PDFSegmenter", install_requirements=True, name="segmenter")
)

with flow:
  indexed_docs = flow.index(docs)