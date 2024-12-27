## Author: Daniella Seum, dseum2023@my.fit.edu
## Course: CSE 2050, Fall 2024
## Project: Height Ordering, week 4, problem A

def insertion_index(line, height):
    low, high = 0, len(line)
    while low < high:
        mid = (low + high) // 2
        if line[mid] <= height:
            low = mid + 1
        else:
            high = mid
    return low

P = int(input())
for _ in range(P):
    data = list(map(int, input().split()))
    K = data[0]
    heights = data[1:]
    line = []
    total_steps = 0
    for height in heights:
        index = insertion_index(line, height)
        steps_back = len(line) - index
        total_steps += steps_back
        line.insert(index, height)
    print(f"{K} {total_steps}")
