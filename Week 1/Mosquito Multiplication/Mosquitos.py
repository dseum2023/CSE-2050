## Author: Daniella Seum, dseum2023@my.fit.edu
## Course: CSE 2050, Fall 2024
## Project: Mosquitos, week 1, problem G
import sys

def num_mosquitos(M, P, L, E, R, S, N):
    for _ in range(N):
        newLarvae = M * E   
        newPupae = L // R   
        newMosquitoes = P // S 
        
        L = newLarvae
        P = newPupae
        M = newMosquitoes
    
    return M

for line in sys.stdin:
    if line.strip():
        M, P, L, E, R, S, N = map(int, line.split())
        result = num_mosquitos(M, P, L, E, R, S, N)
        print(result)