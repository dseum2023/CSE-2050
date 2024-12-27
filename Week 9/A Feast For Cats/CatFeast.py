## Author: Daniella Seum, dseum2023@my.fit.edu
## Course: CSE 2050, Fall 2024
## Project: A Feast for Cats, Week 10, Problem E

import heapq

def allofthecats():
    milk, cats = map(int, input().split())

    ## more cats than milk or milk is less than 1, NO
    if cats > milk or milk < 1:
        print("no")
        return

    A = [[] for _ in range(cats)]
    for _ in range(cats * (cats - 1) // 2):
        i, j, D_ij = map(int, input().split())
        A[i].append((D_ij, j))  ## dist cat i to cat j
        A[j].append((D_ij, i))  ## dist vice versa

    he_need_some_milk = 0  ## milk needed
    visited = set()  ## already visited,fed, and pet the cat
    min_heap = [(0, 0)] 

    ## prims algorithm
    while min_heap:
        ## next cat to feed
        current_distance, cat = heapq.heappop(min_heap)

        ## skip if visited already 
        if cat in visited:
            continue

        ## this one visited
        visited.add(cat)

        he_need_some_milk += current_distance + 1

        ## not enough milk (the cats are angry)
        if he_need_some_milk > milk:
            print("no")
            return

        #explore neighbors
        for distance, neighbor in A[cat]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (distance, neighbor))

    print("yes")

T = int(input())

for _ in range(T):
    allofthecats()  ## aristocats
