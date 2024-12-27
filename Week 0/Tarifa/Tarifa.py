## Author:  Daniella Seum, dseum2023@my.fit.edu
## Course:  CSE 2050, Fall 2024
## Project: Tarifa, week 0, problem B

# X = number of megabytes a month
# N = num of lines
x = int(input())
N = int(input())
total = x
for i in range(N):
   p = int(input())
   total += x-p
print(total)