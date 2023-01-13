
from jina import Executor, requests




class ChunkMerger(Executor):
    @requests(on="/index")
    def merge_chunks(self, docs, **kwargs):
        for doc in docs:  # level 0 document
            for chunk in doc.chunks:
                if doc.text:
                    docs.pop(chunk.id)
            doc.chunks = doc.chunks[...]