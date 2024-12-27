## Author: Daniella Seum, dseum2023@my.fit.edu
## Course: CSE 2050, Fall 2024
## Project: shpoaholic, week 7, problem A

n=int(input())
p= list(map(int,input().split()))

p.sort()
p.reverse()
disc = 0
c = 0

for x in p:
  c += 1
  if c % 3 == 0:
   disc += x
print(disc) 
