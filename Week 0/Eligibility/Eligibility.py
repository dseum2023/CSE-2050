## Author:  Daniella Seum, dseum2023@my.fit.edu
## Course:  CSE 2050, Fall 2024
## Project: Eligibility, week 0, problem E

def eligibile(studentInfo):
    name, startDate, birthDate, courses = studentInfo
    startYear = int(startDate.split('/')[0])
    birthYear = int(birthDate.split('/')[0])
    courses = int(courses)
    
    if startYear >= 2010:
        return f"{name} eligible"
    
    if birthYear >= 1991:
        return f"{name} eligible"
    
    if courses >= 41:
        return f"{name} ineligible"
    
    return f"{name} coach petitions"

n = int(input())
 

results = []
for _ in range(n):
    studentInfo = input().split()
    result = eligibile(studentInfo)
    results.append(result)

    
for result in results:
    print(result)
