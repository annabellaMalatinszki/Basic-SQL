import os
from ui import *


def main():
    while True:
        os.system("clear")
        print_menu()
        try:
            select_menu()
        except KeyError:
            print("Error: No such option")


if __name__ == '__main__':
    main()
