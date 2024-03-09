#!/usr/bin/env python3


import os
import glob
from typing import List
from config import *


class FilteredList:
    def __init__(self, ignored_files: List[str] = []):
        self.config = Manager
        self.ignored_files = ignored_files


    def files(self) -> List[str]:
        all_files = []

        for extension in self.config.loader_mapping:
            all_files.extend(glob.glob(os.path.join(
                self.config.source_dir, f"**/*{extension}"), recursive=True))

        filtered_files = [
            file_path for file_path in all_files if file_path not in self.ignored_files]

        return filtered_files
