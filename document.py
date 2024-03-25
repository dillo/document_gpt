#!/usr/bin/env python3

import os
import glob
from langchain.docstore.document import Document
from typing import List
from config import *


class Document:
    def __init__(self, file_path: str):
        self.file_path = file_path


    def load(self) -> List[Document]:
        loader = self.loader(self.file_path)

        return loader.load()


    def filter(self) -> List[str]:
        all_files = []

        for extension in self.config.loader_mapping:
            all_files.extend(glob.glob(os.path.join(
                self.config.source_dir, f"**/*{extension}"), recursive=True))

        filtered_files = [
            file_path for file_path in all_files if file_path not in self.ignored_files]

        return filtered_files


    def loader(self):
        return self.config.loader_mapping[self.extension]


    def extension(self) -> str:
        parts = os.path.splitext(self.file_path)

        return parts[1]
