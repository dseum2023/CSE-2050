## Author: Daniella Seum, dseum2023@my.fit.edu
## Course: CSE 2050, Fall 2024
## Project: Texas Summers, Week 10, Problem B
import sys
import heapq
import math

input = sys.stdin.read
data = input().splitlines()

## num shady spots
n = int(data[0])

## list to store nodes 
nodes = []
for i in range(1, n + 1):
    x, y = map(int, data[i].split())
    nodes.append((x, y))

x, y = map(int, data[n + 1].split())
nodes.insert(0, (x, y))  ## dorm at index 0

x, y = map(int, data[n + 2].split())
nodes.append((x, y))  ## class at index n+1

## total nodes
V = n + 2  

K = 20  ## number of nearest neighbors to consider
m = 50  ## range of nodes to check

## adjacency list for graph representation
A = [[] for _ in range(V)]

## sort nodes by x and y coordinates
nodes_x = sorted((x, y, idx) for idx, (x, y) in enumerate(nodes))
nodes_y = sorted((y, x, idx) for idx, (x, y) in enumerate(nodes))

## store index of node 
index_in_x = [0] * V
index_in_y = [0] * V

for pos, (x, y, idx) in enumerate(nodes_x):
    index_in_x[idx] = pos

for pos, (y, x, idx) in enumerate(nodes_y):
    index_in_y[idx] = pos

for u in range(V):
    potential_neighbors = set()  ## stores potential neighbors for node u
    pos_x = index_in_x[u]
    ## check x
    for i in range(max(0, pos_x - m), min(V, pos_x + m + 1)):
        if i == pos_x:
            continue
        x2, y2, v = nodes_x[i]
        potential_neighbors.add(v)
    pos_y = index_in_y[u]
    ## check y
    for i in range(max(0, pos_y - m), min(V, pos_y + m + 1)):
        if i == pos_y:
            continue
        y2, x2, v = nodes_y[i]
        potential_neighbors.add(v)
    x1, y1 = nodes[u]
    neighbors = []
    ## calculate distances 
    for v in potential_neighbors:
        x2, y2 = nodes[v]
        dx = x1 - x2  # change in x
        dy = y1 - y2  # change in y
        distance = math.hypot(dx, dy)  #distance
        neighbors.append((distance, v))
    neighbors.sort()  ## sort neighbors by distance
    ## add K nearest neighbors to adjacency list
    for dist, v in neighbors[:K]:
        cost = dist ** 3  # cost=distance^3
        A[u].append((v, cost))

## distance array for shortest path
dist = [float('inf')] * V

## previous node array for path reconstruction
prev = [None] * V

dist[0] = 0  

## priority queue 
hq = [(0, 0)]  

## Dijkstra's algorithm for shortest path
while hq:
    cost_u, u = heapq.heappop(hq)  ## pop node w/ least cost
    if cost_u > dist[u]: 
        continue
    for v, cost in A[u]:
        if dist[v] > dist[u] + cost:  ## check if shorter path found
            dist[v] = dist[u] + cost  ## update shortest distance to v
            prev[v] = u  ## update previous node for v
            heapq.heappush(hq, (dist[v], v))  ## push updated cost to queue

## reconstruct shortest path from dorm to class
path = []
u = n + 1  ## class node
while u is not None:
    path.append(u)
    u = prev[u]
path.reverse()  ## reverse for dorm to class


shade = []
for u in path[1:-1]:  
    if 1 <= u <= n:  
        shade.append(u - 1) 

if not shade:
    print('-')  ## no shady spots found
else:
    for idx in shade:
        print(idx) 