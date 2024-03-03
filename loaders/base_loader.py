#!/usr/bin/env python3


from typing import List
from langchain.docstore.document import Document


class BaseLoader:
    def __init__(self, file_path: str, **kwargs):
        self.file_path = file_path
        self.loader_args = kwargs

    def load(self) -> List[Document]:
        return self.loader.load()
