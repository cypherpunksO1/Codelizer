from dataclasses import dataclass
from src.utils import format_number


@dataclass
class Ignore:
    files: list[str] = list
    folders: list[str] = list
    files_extensions: list[str] = list


@dataclass
class Analyze:
    files_count: int = 0
    lines_count: int = 0
    folders_count: int = 0
    tree: dict = None
    
    
    def __iter__(self):
        return iter([
            format_number(self.lines_count),
            format_number(self.files_count), 
            format_number(self.folders_count)
        ])
    