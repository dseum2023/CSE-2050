## Author: Daniella Seum, dseum2023@my.fit.edu
## Course: CSE 2050, Fall 2024
## Project: EpigDanceOff, week 3, problem c

def count_dance_moves():
    N, M = map(int, input().split()) 
    grid = [input().strip() for _ in range(N)]  
    
    move_count = 1
    in_blank_column_group = False  
    

    for col in range(M):
        is_blank = all(grid[row][col] == '_' for row in range(N))
        
        if is_blank:
            if not in_blank_column_group:
                move_count += 1
                in_blank_column_group = True  
        else:
            in_blank_column_group = False
    
    print(move_count)

count_dance_moves()
