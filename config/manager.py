#!/usr/bin/env python3

import os
from loaders import *


class Manager:
    def __init__(self):
        self.model = os.environ.get("MODEL", "mistral")
        self.persist_directory = os.environ.get(
            'PERSIST_DIRECTORY', 'database')
        self.source_directory = os.environ.get(
            'SOURCE_DIRECTORY', 'documents')
        self.embeddings_model_name = os.environ.get(
            "EMBEDDINGS_MODEL_NAME", "all-MiniLM-L6-v2")
        self.target_source_chunks = int(
            os.environ.get('TARGET_SOURCE_CHUNKS', 4))
        self.chunk_size = 512
        self.chunk_overlap = 64
        self.loader_mapping = {
            ".csv": MyCSVLoader,
            ".pdf": MyPDFLoader,
            ".eml": MyEmlLoader,
            ".txt": MyTextLoader,
            ".doc": MyDocLoader,
            ".docx": MyDocLoader,
            ".ppt": MyPPTLoader,
            ".pptx": MyPPTLoader,
            ".odt": MyODTLoader,
            ".md": MyMarkdownLoader,
            ".html": MyHTMLLoader,
        }
