import time
import sys
from termcolor import colored
from tqdm import tqdm
import os

# Formatting of command: 
# python timer.py n_cycles len_work len_break
sysargs = [str(x) for x in sys.argv]
#first arg is gonna be timer.py
n_cycles = int(sysargs[1])
len_work = int(sysargs[2])
len_break = int(sysargs[3])

# time.sleep(t) works with t *seconds*

clr = lambda: os.system('cls')

for n in range(n_cycles):
    if n_cycles>1: print(colored(f"Cycle {n+1} of {n_cycles} cycles with {len_work} minute(s) working and {len_break} minute(s) on break per cycle", 'blue')) 
    
    print(colored(f"Work Time! Try to focus on your work for {len_work} minute(s)", 'green'))
    for i in tqdm(range(4*len_work), desc="Working time"):
        time.sleep(15) # sleep 15 seconds
    print(colored(f"Break Time! {len_break} minute(s) off", 'blue'))
    for i in tqdm(range(4*len_break), desc="Break time"):
        time.sleep(15)
    clr()


