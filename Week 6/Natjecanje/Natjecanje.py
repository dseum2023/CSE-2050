## Author: Daniella Seum, dseum2023@my.fit.edu
## Course: CSE 2050, Fall 2024
## Project: Natjecanje, week 6, problem D

def kayak_check(damaged, reserves):
    cant_compete = 0

    damaged_list = damaged.copy()
    reserves_list = reserves.copy()

    for kayak in reserves_list:
        if kayak in damaged_list:
            damaged_list.remove(kayak)
            reserves.remove(kayak)
        elif (kayak - 1) in damaged_list:
            damaged_list.remove(kayak - 1)
            reserves.remove(kayak)
        elif (kayak + 1) in damaged_list:
            damaged_list.remove(kayak + 1)
            reserves.remove(kayak)
    
    cant_compete = len(damaged_list)
    return cant_compete

N, S, R = map(int, input().split())

damaged = list(map(int, input().split()))
reserves = list(map(int, input().split()))

print(kayak_check(damaged, reserves))
