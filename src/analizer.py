from argparse import Namespace as Args

from src.schemas import Analyze
from src.ignore import read_ignore

import os


def get_file_lines(file_path: str) -> int:
    """ Get file lines amouns. """
    
    try:
        with open(file_path, 'r') as file:
            try:
                return sum(1 for line in file)
            except UnicodeDecodeError:
                return 0
    except (PermissionError, FileNotFoundError):
            return 0
        
        
def analyze_file(flags: Args
                 ) -> Analyze | None:
    """ Analize one file. """
    
    if flags.file:
        total_lines = get_file_lines(file_path=flags.file)
        return Analyze(lines_count=total_lines)
    
    return


def check_file_extension(file: str, 
                         extensions: str) -> bool:
    """ Check file extension on ignore file. """
    
    file_extension = file.split('.')
    if len(file_extension) > 1:
        file_extension = file_extension[-1]
        return file_extension not in extensions


def analize(directory_path: str, 
            flags: Args) -> Analyze:
    """ Get analyze objects. """
    
    analyze_file_result = analyze_file(flags=flags)
    if analyze_file_result: 
        return analyze_file_result
    
    directory_path = flags.dir if flags.dir else directory_path
    total_lines, total_files, total_folders = (0, 0, 0)
    ignore = read_ignore(directory_path=directory_path, 
                         flags=flags)
    
    tree = dict()

    for root, dirs, files in os.walk(directory_path):
        total_folders += len(dirs)
        
        dirs[:] = [d for d in dirs if d not in ignore.folders]
        
        for file in files:
            if file not in ignore.files and \
                check_file_extension(file=file, 
                                     extensions=ignore.files_extensions):
                total_files += 1
                total_lines += get_file_lines(file_path=os.path.join(root, file))
                tree[file] = total_lines
            
    return Analyze(files_count=0 if flags.exf else total_files, 
                   lines_count=0 if flags.exl else total_lines, 
                   folders_count=0 if flags.exd else total_folders, 
                   tree=tree)
