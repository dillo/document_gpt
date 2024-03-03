#!/usr/bin/env python3


import os
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from config import *


class VectorStoreManager:
    def __init__(self, config: ConfigurationManager):
        self.config = config
        self.embeddings = HuggingFaceEmbeddings(
            model_name=self.config.embeddings_model_name)

    def does_vectorstore_exist(self) -> bool:
        index_directory = os.path.join(self.config.persist_directory, 'index')
        return os.path.exists(index_directory)

    def update_or_create_store(self, texts):
        if self.does_vectorstore_exist():
            print(
                f"Appending to existing vectorstore at {self.config.persist_directory}")
            db = Chroma(persist_directory=self.config.persist_directory,
                        embedding_function=self.embeddings)
            db.add_documents(texts)
        else:
            print("Creating new vector")
