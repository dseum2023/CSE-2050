## Author: Daniella Seum, dseum2023@my.fit.edu
## Course: CSE 2050, Fall 2024
## Project: Flipping Patties, week 3, problem B

def minimum_cooks_needed(orders):
    
    timeline = {}
    
    for d, t in orders:
        start_time = t - 2 * d
        flip_time = t - d
        serve_time = t
        
        timeline[start_time] = timeline.get(start_time, 0) + 1
        
        timeline[flip_time] = timeline.get(flip_time, 0) + 1
        
        timeline[serve_time] = timeline.get(serve_time, 0) + 1

    max_actions_per_second = max(timeline.values())
    
    return (max_actions_per_second + 1) // 2


n = int(input())
orders = [tuple(map(int, input().split())) for _ in range(n)]

print(minimum_cooks_needed(orders))
