## Author: Daniella Seum, dseum2023@my.fit.edu
## Course: CSE 2050, Fall 2024
## Project: Mastering Mastermind, week 3, problem A

def check(n, code, guess):
    r = 0
    remaining_code = []
    remaining_guess = []
    
    for i in range(n):
        if code[i] == guess[i]:
            r += 1
        else:
            remaining_code.append(code[i])
            remaining_guess.append(guess[i])
    
    s = 0
    for char in remaining_guess:
        if char in remaining_code:
            s += 1
            remaining_code.remove(char) 
    

    return r, s


n, code, guess = input().split()
n = int(n)


r, s = check(n, code, guess)
print(r, s)