#!/usr/bin/env python3


from config import *


class LoaderType:
    def __init__(self, config: Manager, extension: str):
        self.config = config
        self.extension = extension

    def select_type(self):
        return self.config.loader_mapping[self.extension]
