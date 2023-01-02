





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


