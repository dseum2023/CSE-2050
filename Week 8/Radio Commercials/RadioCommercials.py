## Author: Daniella Seum, dseum2023@my.fit.edu
## Course: CSE 2050, Fall 2024
## Project: Radio Commercials, Week 8, Problem A

def commercials(n,p,arr):
    prof = []
    for i in range(n):
        prof.append(arr[i]-p)
    maxi = prof[0]
    curr = prof[0]
    for i in range(1,n):
        curr =max(prof[i],curr+prof[i])
        if curr>maxi:
            maxi=curr
    print(maxi)
    
n,p = map(int,input().split())
arr = list(map(int,input().split()))
commercials(n,p,arr)
