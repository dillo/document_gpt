#!/usr/bin/env python3

from typing import List
from langchain.docstore.document import Document
from langchain_community.document_loaders import UnstructuredEmailLoader


class MyEmlLoader(UnstructuredEmailLoader):
    def load(self) -> List[Document]:
        try:
            doc = self._load_email()
        except Exception as e:
            raise type(e)(f"{self.file_path}: {e}") from e

        return doc

    def _load_email(self) -> List[Document]:
        try:
            doc = UnstructuredEmailLoader.load(self)
        except ValueError as e:
            if 'text/html content not found in email' in str(e):
                self.unstructured_kwargs["content_source"] = "text/plain"
                doc = UnstructuredEmailLoader.load(self)
            else:
                raise

        return doc
