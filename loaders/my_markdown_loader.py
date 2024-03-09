#!/usr/bin/env python3


from langchain_community.document_loaders import UnstructuredMarkdownLoader
from loaders.base_loader import BaseLoader


class MyMarkdownLoader(BaseLoader):
    def __init__(self, file_path: str, **kwargs):
        super().__init__(file_path, **kwargs)
        self.loader = UnstructuredMarkdownLoader(file_path, **kwargs)
