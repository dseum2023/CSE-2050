## Author:  Daniella Seum, dseum2023@my.fit.edu
## Course:  CSE 2050, Fall 2024
## Project: Combination Lock, week 1, problem A

def calculate_degrees(p, a, b, c):
    degrees = 720  # 2 full turns
    # Turn to the first number
    degrees += ((p - a) % 40) * 9
    # 1 full turn
    degrees += 360
    # turning to the second number
    degrees += ((b - a) % 40) * 9
    # Turn to the third number
    degrees += ((b - c) % 40) * 9
    
    return degrees

while True:
    p, a, b, c = map(int, input().split())
    if p == 0 and a == 0 and b == 0 and c == 0:
        break
    print(calculate_degrees(p, a, b, c))
