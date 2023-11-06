from src.schemas import Analyze
from prettytable import PrettyTable
import time


def printer(analyze: Analyze, 
            tree: bool, 
            directory_path: str, 
            scan_start: float) -> None:
    
    print("\n➤ " + directory_path + "\n")
    
    if tree:
        tree_table = PrettyTable()
        tree_table.field_names = ["File", "Lines"]
        
        for branch in analyze.tree:
            tree_table.add_row([branch, analyze.tree[branch]])
            
        print("\n" + str(tree_table) + "\n")
    
    stats_table = PrettyTable()
    stats_table.field_names = ["lines", "files", "folders"]
    stats_table.add_row(list(analyze))
    
    print("\n" + str(stats_table) + "\n")
    print(f"➤ Scan time: {round(time.time() - scan_start, 1)}s.\n\n")
