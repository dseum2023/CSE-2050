## Author: Daniella Seum, dseum2023@my.fit.edu
## Course: CSE 2050, Fall 2024
## Project: Batter Up, week 1, problem B

n = int(input().strip())
hits = list(map(int, input().strip().split()))

total = 0
count = n

for hit in hits:
    if hit == -1:
        count -= 1
    else:
        total += hit

if count > 0:
    batting_average = total / count
else:
    batting_average = 0

print(batting_average)
