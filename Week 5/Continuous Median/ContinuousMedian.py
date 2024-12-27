## Author: Daniella Seum, dseum2023@my.fit.edu
## Course: CSE 2050, Fall 2024
## Project: Continuous median, week 5, problem D
import sys
import heapq

T_line = ''
while T_line.strip() == '':
    T_line = sys.stdin.readline()
T = int(T_line)

for _ in range(T):
    N_line = ''
    while N_line.strip() == '':
        N_line = sys.stdin.readline()
    N = int(N_line)
    
    while True:
        A_line = sys.stdin.readline()
        if A_line.strip() != '':
            break
    A = list(map(int, A_line.strip().split()))
    while len(A) < N:
        A_line = sys.stdin.readline()
        A.extend(map(int, A_line.strip().split()))
    
    max_heap = []
    min_heap = []
    sum_medians = 0

    for num in A[:N]:
        if not max_heap or num <= -max_heap[0]:
            heapq.heappush(max_heap, -num)
        else:
            heapq.heappush(min_heap, num)

        if len(max_heap) > len(min_heap) + 1:
            moved_num = -heapq.heappop(max_heap)
            heapq.heappush(min_heap, moved_num)
        elif len(min_heap) > len(max_heap):
            moved_num = heapq.heappop(min_heap)
            heapq.heappush(max_heap, -moved_num)

        if len(max_heap) == len(min_heap):
            median = (-max_heap[0] + min_heap[0]) // 2
        else:
            median = -max_heap[0]

        sum_medians += median

    print(sum_medians)
