## Author: Daniella Seum, dseum2023@my.fit.edu
## Course: CSE 2050, Fall 2024
## Project: CD, week 5, problem A

while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:  # End of input condition
        break

    Jack = set()  # Using sets for faster lookup
    Jill = set()

    for _ in range(N):
        Jack.add(int(input()))  # Store Jack's CDs in a set
    
    for _ in range(M):
        Jill.add(int(input()))  # Store Jill's CDs in a set

    duplicates = len(Jack.intersection(Jill))  # Find common CDs

    print(duplicates)
