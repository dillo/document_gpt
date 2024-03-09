#!/usr/bin/env python3


import os
from typing import List


class Extension:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def get_extension(self) -> str:
        parts = os.path.splitext(self.file_path)

        return parts[1]
