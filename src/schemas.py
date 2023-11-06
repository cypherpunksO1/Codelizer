from dataclasses import dataclass


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
            self.lines_count,
            self.files_count, 
            self.folders_count
        ])
    