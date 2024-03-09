#!/usr/bin/env python3

from config import *
from files import *


def main():
    """
    Entry point of the program.

    This function initializes the configuration manager, document processor, and vector store manager.
    It processes the documents, and updates or creates the vector store based on the processed texts.
    """
    config = Manager()
    processor = Processor(config)
    vector_store_manager = VectorStoreManager(config)
    texts = processor.process_documents()
    vector_store_manager.update_or_create_store(texts)


if __name__ == "__main__":
    main()
