import os
import time
from itertools import cycle
import random

def blinking_tree():
    tree = [
        "        *        ",
        "       ***       ",
        "      *****      ",
        "     *******     ",
        "    *********    ",
        "   ***********   ",
        "  *************  ",
        "       |||       ",
        "                 ",
        "                 ",
        "                 ",
        "           .less ",
    ]

    lights = cycle(["\033[91m*\033[0m", "\033[93m*\033[0m", "\033[92m*\033[0m", "\033[94m*\033[0m", "\033[95m*\033[0m"])
    reset = "\033[0m"
    
    try:
        while True:
            os.system("clear")
            for i, line in enumerate(tree):
                if i in range(1, 7):
                    line = ''.join(
                        next(lights) if char == '*' and random.choice([True, False]) else char
                        for char in line
                    )
                print(line)
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("\nMerry Christmas! 🎄 by .less")

if __name__ == "__main__":
    blinking_tree()
