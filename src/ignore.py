from argparse import Namespace as Args

from src.schemas import Ignore
from src.flags import get_flags
from src.config import IGNORE_F_NAME

import os


def search_ignore_file(ignore_name: str, 
                       directory_path: str
                       ) -> list:
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file == ignore_name:
                with open(ignore_name, 'r') as file:
                    return file.readlines()


def read_ignore(directory_path: str, 
                flags: Args
                ) -> Ignore:
    if flags.ignore:
        lines = search_ignore_file(ignore_name=flags.ignore, 
                                   directory_path=directory_path)
    else:
        lines = search_ignore_file(ignore_name=IGNORE_F_NAME, 
                                   directory_path=directory_path)
                
    if lines:
        folders = list()
        files = list()
        files_extensions = list()
        
        for line in lines:
            if line.strip().endswith('/'):
                folders.append(line[:-2].strip())
            elif line.startswith("*"):
                files_extensions.append(line.split("*.")[1].strip())
            else:
                files.append(line.strip())
            
        return Ignore(files=files, 
                      files_extensions=files_extensions,
                      folders=folders)
        
    return Ignore(list(), 
                  list())