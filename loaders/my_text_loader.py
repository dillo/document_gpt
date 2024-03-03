#!/usr/bin/env python3


from typing import List
from langchain.docstore.document import Document
from langchain_community.document_loaders import TextLoader
from loaders.base_loader import BaseLoader


class MyTextLoader(BaseLoader):
    def __init__(self, file_path: str, **kwargs):
        super().__init__(file_path, **kwargs)
        self.loader = TextLoader(file_path, **kwargs)
