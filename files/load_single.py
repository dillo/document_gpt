#!/usr/bin/env python3


from langchain.docstore.document import Document
from typing import List


class LoadSingle:
    def __init__(self, loader_type, file_path: str):
        self.loader_type = loader_type
        self.file_path = file_path

    def load(self) -> List[Document]:
        loader = self.loader_type(self.file_path)

        return loader.load()
