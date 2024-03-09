#!/usr/bin/env python3


from langchain_community.document_loaders import UnstructuredHTMLLoader
from loaders.base_loader import BaseLoader


class MyHTMLLoader(BaseLoader):
    def __init__(self, file_path: str, **kwargs):
        super().__init__(file_path, **kwargs)
        self.loader = UnstructuredHTMLLoader(file_path, **kwargs)
