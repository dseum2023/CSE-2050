## Author: Daniella Seum, dseum2023@my.fit.edu
## Course: CSE 2050, Fall 2024
## Project: firefly, week 7, problem B

N , H = map(int,input().split())
arr=[0]*(H+2)

for i in range(N):
 k = int(input()) 
 
 if i%2==0: ##even
  arr[1]+=1
  arr[k+1]-=1
  
 else:
  arr[H-k+1]+=1
  arr[H+1]-=1
  
for i in range(1,H+1):
 arr[i]=arr[i]+arr[i-1]
 
minimum = min(arr[1:H+1])
c = arr[1:H+1].count(minimum)
print(minimum, c)
