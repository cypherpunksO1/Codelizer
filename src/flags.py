from src.config import IGNORE_F_NAME
import argparse


def get_flags():
    parser = argparse.ArgumentParser()

    parser.add_argument('--dir', 
                        type=str, 
                        help='Other dir')
    
    parser.add_argument("--file", 
                        type=str, 
                        help="Get file lines count")
    
    parser.add_argument("--ignore", 
                        type=str, 
                        help=f"Set new {IGNORE_F_NAME}")
    
    parser.add_argument("-tree", 
                        action='store_true', 
                        help="View files tree")
    
    
    parser.add_argument("-exd", 
                        action='store_true', 
                        help="Exclude directories count from table")
    
    parser.add_argument("-exf", 
                        action='store_true', 
                        help="Exclude files count from table")
    
    parser.add_argument("-exl", 
                        action='store_true', 
                        help="Exclude lines count from table")

    args = parser.parse_args()
    
    return args
