#!/usr/bin/env python3


from langchain_community.document_loaders import PyMuPDFLoader
from loaders.base_loader import BaseLoader


class MyPDFLoader(BaseLoader):
    def __init__(self, file_path: str, **kwargs):
        super().__init__(file_path, **kwargs)
        self.loader = PyMuPDFLoader(file_path, **kwargs)
