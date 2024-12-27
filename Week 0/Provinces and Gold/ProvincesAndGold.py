## Author:  Daniella Seum, dseum2023@my.fit.edu
## Course:  CSE 2050, Fall 2024
## Project: Provinces and Gold, week 0, problem C

numGold, numSilver, numCopper = map(int, input().split())
buyingPower = (numGold*3) + (numSilver*2) + numCopper
i = 0
while (i==0):
    if buyingPower < 2:
        print('Copper', end='')
        break
    
    if buyingPower >= 8:
        print('Province',  end='')
    elif buyingPower < 8 and buyingPower >= 5:
        print('Duchy',  end='')
    else:
        print('Estate',  end='')
    
    print(' or ',  end='')

    if buyingPower >= 6:
        print('Gold',  end='')
    elif buyingPower < 6 and buyingPower >= 3:
        print('Silver',  end='')
    else:
        print('Copper',  end='')
    
    i = 1
    
    