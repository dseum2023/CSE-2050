## Author: Daniella Seum, dseum2023@my.fit.edu
## Course: CSE 2050, Fall 2024
## Project: boss battle, week 1, problem D
import math

def bombs(n):
    if n <= 3:
        return 1
    else:
        return n-2
    
n = int(input())
print(bombs(n))
