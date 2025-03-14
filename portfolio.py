pip install colorama
from colorama import Fore, Style, init
import time

# Initialize Colorama
init(autoreset=True)

# List of colors
colors = [
    Fore.RED,
    Fore.GREEN,
    Fore.YELLOW,
    Fore.BLUE,
    Fore.MAGENTA,
    Fore.CYAN,
    Fore.WHITE,
    Fore.LIGHTBLACK_EX,
    Fore.LIGHTCYAN_EX,
    Fore.LIGHTMAGENTA_EX
]

# Header for the portfolio
print(Fore.BLUE + "Welcome to David Bassey's Portfolio!\n")

# Loop to print "I love you" in different colors
for i in range(10):
    print(colors[i % len(colors)] + "I love you from David Bassey!")
    time.sleep(0.5)  # Pause for half a second

