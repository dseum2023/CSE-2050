## Author: Daniella Seum, dseum2023@my.fit.edu
## Course: CSE 2050, Fall 2024
## Project: Bubble Tea, week 1, problem c


n = int(input().strip())  
priceTea = list(map(int, input().strip().split()))  

m = int(input().strip())  
priceTopping = list(map(int, input().strip().split()))  

minCost = float('inf')  


for _ in range(n):
    line = list(map(int, input().strip().split()))
    k = line[0]  
    toppings = line[1:]  

    teaIndex = _  
    teaPrice = priceTea[teaIndex]
    
    for topping in toppings:
        toppingIndex = topping - 1  
        toppingPrice = priceTopping[toppingIndex]
        
        totalCost = teaPrice + toppingPrice
        
        if totalCost < minCost:
            minCost = totalCost


money = int(input().strip())


if minCost > money:
    print(0)
else:
    students = (money // minCost) - 1
    print(students)
