from typing import IO
import sys

def say(*values: object, sep: str = ' ', end: str = '\n', file: IO = None):
    """this is the recreation of the print function"""
    if file:
        with open(file, 'w') as f:
            sys.stdout = f  
            for value in values:
                f.write(f"{value}{sep}")
            f.write(end)
        f.close()
        
    else:
        for value in values:
            sys.stdout.write(f"{value}{sep}")
        sys.stdout.write(end)

def measure(value, end: str ="\n") -> int:
    """this is a recreation of the len function"""
    count = 0
    for x in value:
        count+=1
    return count
