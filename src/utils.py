from src.config import (IGNORE_F_NAME, 
                        BASE_IGNORE_TEMPLATE)


def format_number(number):
    formatted_number = "{:,}".format(number).replace(",", " ")
    return formatted_number


def make_ignore():
    with open(IGNORE_F_NAME, 'w') as file:
        file.write(BASE_IGNORE_TEMPLATE)
        
    print("\n\n> " + IGNORE_F_NAME, "created", end="\n\n\n")
