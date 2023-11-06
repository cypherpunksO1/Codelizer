from src.config import (IGNORE_F_NAME, 
                        BASE_IGNORE_TEMPLATE)
import os
from colorama import Fore, Style


def print_directory_contents(path, 
                             indent='    ', 
                             first: bool = True):
    children = os.listdir(path)
    
    if first:
        print(f'{Fore.GREEN}{path.split("/")[-1]} ➤ {Style.RESET_ALL}')
    
    for index, child in enumerate(children):
        child_path = os.path.join(path, child)
        if os.path.isdir(child_path):
            print(f'{indent}{Fore.GREEN}{child} ➤{Style.RESET_ALL}')
            print_directory_contents(child_path, 
                                     indent + f'{Fore.GREEN}⎮{Style.RESET_ALL}   ',
                                     False)
        else:
            print(f'{indent}{Fore.LIGHTBLACK_EX}{child}{Style.RESET_ALL}')


def make_ignore():
    with open(IGNORE_F_NAME, 'w') as file:
        file.write(BASE_IGNORE_TEMPLATE)
        
    print("\n\n> " + IGNORE_F_NAME, "created", end="\n\n\n")