## Author: Daniella Seum, dseum2023@my.fit.edu
## Course: CSE 2050, Fall 2024
## Project: ACM Contest, week 1, problem F

def contest_ranking(entries):
    solved = {}
    totalSolved = 0
    totalTime = 0
    
    for entry in entries:
        if entry == "-1":
            break
        
        time, problem, result = entry.split()
        time = int(time)
        
        if problem not in solved:
            solved[problem] = {'penalty': 0, 'solved': False}
        
        if result == "right" and not solved[problem]['solved']:
            solved[problem]['solved'] = True
            totalSolved += 1
            totalTime += time + solved[problem]['penalty']
        
        elif result == "wrong" and not solved[problem]['solved']:
            solved[problem]['penalty'] += 20
    
    return totalSolved, totalTime
entries = []
while True:
    entry = input()
    entries.append(entry)
    if entry == "-1":
        break

numSolved, totalTime = contest_ranking(entries)

print(numSolved, totalTime)