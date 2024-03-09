#!/usr/bin/env python3


from langchain_community.document_loaders import UnstructuredEPubLoader
from loaders.base_loader import BaseLoader


class MyEpubLoader(BaseLoader):
    def __init__(self, file_path: str, **kwargs):
        super().__init__(file_path, **kwargs)
        self.loader = UnstructuredEPubLoader(file_path, **kwargs)
