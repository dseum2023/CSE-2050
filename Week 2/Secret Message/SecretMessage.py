## Author: Daniella Seum, dseum2023@my.fit.edu
## Course: CSE 2050, Fall 2024
## Project: Secret Message, week 2, problem D
import math

def encrypt_message(message):
    # Step 1: Find the length of the message
    L = len(message)
    
    # Step 2: Find the smallest square number M >= L
    K = math.ceil(math.sqrt(L))
    M = K * K
    
    # Step 3: Pad the message with asterisks to length M
    padded_message = message.ljust(M, '*')
    
    # Step 4: Create the grid
    grid = []
    for i in range(K):
        grid.append(list(padded_message[i*K:(i+1)*K]))
    
    # Step 5: Rotate the grid 90 degrees clockwise
    rotated_grid = []
    for col in range(K):
        new_row = []
        for row in range(K-1, -1, -1):
            new_row.append(grid[row][col])
        rotated_grid.append(new_row)
    
    # Step 6: Read the message from the rotated grid, ignoring asterisks
    secret_message = ''.join(rotated_grid[i][j] for i in range(K) for j in range(K) if rotated_grid[i][j] != '*')
    
    return secret_message



# Read number of test cases
n = int(input())
    
# Process each test case
for _ in range(n):
    message = input().strip()
    print(encrypt_message(message))