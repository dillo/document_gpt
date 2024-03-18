#!/usr/bin/env python3

import os
from langchain.docstore.document import Document
from typing import List


class Document:
    def __init__(self, loader_type, file_path: str):
        self.file_path = file_path
        self.loader_type = loader_type

    def extension(self) -> str:
        parts = os.path.splitext(self.file_path)

        return parts[1]

    def load(self) -> List[Document]:
        loader = self.loader_type(self.file_path)

        return loader.load()
