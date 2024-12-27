## Author: Daniella Seum, dseum2023@my.fit.edu
## Course: CSE 2050, Fall 2024
## Project: Gregory the Grasshopper, Week 10, Problem A
from collections import deque
import sys

def operation_GGF(rows, columns, gregg_row, gregg_column, clover_row, clover_column):
    ## 0-based indexing
    gregg_row -= 1
    gregg_column -= 1
    clover_row -= 1
    clover_column -= 1

    ## dont move if already there
    if gregg_row == clover_row and gregg_column == clover_column:
        print(0)
        return

    ## init visited grid
    visited = [[False for _ in range(columns)] for _ in range(rows)]

    ## starting position is visited
    visited[gregg_row][gregg_column] = True

    ## possible moves
    moves = [
        (2, 1), (2, -1), (-2, 1), (-2, -1),
        (1, 2), (1, -2), (-1, 2), (-1, -2)
    ]

    ## BFS queue
    queue = deque()
    queue.append((gregg_row, gregg_column, 0))  # (row, column, distance)

    while queue:
        current_row, current_column, current_hops = queue.popleft()
        ## check all possible moves
        
        for row_change, column_change in moves:
            ## next position
            next_row, next_column = current_row + row_change, current_column + column_change
            
            ## next pos must be in grid and not visisted
            if 0 <= next_row < rows and 0 <= next_column < columns and not visited[next_row][next_column]:
                
                ## if clover position
                if next_row == clover_row and next_column == clover_column:
                    print(current_hops + 1)
                    return
                
                ## mark as visited    
                visited[next_row][next_column] = True
                queue.append((next_row, next_column, current_hops + 1))
                
    print("impossible")


for input_line in sys.stdin:
    input_line = input_line.strip()
    if not input_line:
        continue 

    rows, columns, gregg_row, gregg_column, clover_row, clover_column = map(int, input_line.split())
    
    ## operation get gregory food
    operation_GGF(rows, columns, gregg_row, gregg_column, clover_row, clover_column)
