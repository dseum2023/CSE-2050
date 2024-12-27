## Author: Daniella Seum, dseum2023@my.fit.edu
## Course: CSE 2050, Fall 2024
## Project: Trik, week 2, problem A

def swap(move, position):
    # position 1=left, 2=middle, 3=right
    if move == 'A':
        if position == 1:
            position = 2
        elif position == 2:
            position = 1
    elif move == 'B':
        if position == 3:
            position = 2
        elif position == 2:
            position = 3
    elif move == 'C':
        if position == 3:
            position = 1
        elif position == 1:
            position = 3
    return position

moves = input()

# Initialize position to 1 (left) as stated in the code comment
position = 1

for i in range(len(moves)):
    position = swap(moves[i], position)
    
print(position)
