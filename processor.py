#!/usr/bin/env python3


import glob
import os
from multiprocessing import Pool
from tqdm import tqdm
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document
from typing import List
from config import *


class Processor:
    def __init__(self, config: Manager):
        self.config = config

    def process_documents(self, ignored_files: List[str] = []) -> List[str]:
        print(f"Loading documents from {self.config.source_directory}")

        documents = self.load_documents(
            self.config.source_directory, ignored_files)

        if not documents:
            print("No new documents to load")
            return []

        print(f"Loaded {len(documents)} new documents")

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.config.chunk_size, chunk_overlap=self.config.chunk_overlap)
        texts = text_splitter.split_documents(documents)

        print(f"Split into {len(texts)} chunks of text")

        return texts

    def load_documents(self, source_dir: str, ignored_files: List[str] = []) -> List[Document]:
        all_files = []

        for ext in self.config.loader_mapping:
            all_files.extend(glob.glob(os.path.join(
                source_dir, f"**/*{ext}"), recursive=True))

        filtered_files = [
            file_path for file_path in all_files if file_path not in ignored_files]

        documents = []

        with Pool(processes=os.cpu_count()) as pool, tqdm(total=len(filtered_files), desc='Loading documents', ncols=80) as pbar:
            for docs in pool.imap_unordered(self.load_single_document, filtered_files):
                documents.extend(docs)
                pbar.update()

        return documents

    def load_single_document(self, file_path: str) -> List[Document]:
        ext = os.path.splitext(file_path)[1]

        if ext in self.config.loader_mapping:
            loader_class = self.config.loader_mapping[ext]
            loader = loader_class(file_path)
            return loader.load()

        raise ValueError(f"Unsupported file extension '{ext}'")
