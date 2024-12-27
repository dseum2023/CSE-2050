## Author:  Daniella Seum, dseum2023@my.fit.edu
## Course:  CSE 2050, Fall 2024
## Project: Moscow Dream, week 0, problem D

def isValid(a, b, c, n):
    if a > 0 and b > 0 and c > 0:  
        total_problems = a + b + c
        if total_problems >= n and n >= 3:  
            if (a - 1) + (b - 1) + (c - 1) >= n - 3:
                return "YES"
    return "NO"

a, b, c, n = map(int, input().split())

result = isValid(a, b, c, n)
print(result)
