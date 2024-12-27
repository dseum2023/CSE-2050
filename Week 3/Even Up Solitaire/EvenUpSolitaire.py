## Author: Daniella Seum, dseum2023@my.fit.edu
## Course: CSE 2050, Fall 2024
## Project: Even Up Solitaire, week 3, problem D

def even(cards):
    stack = []
    for card in cards:
        if stack and (stack[-1] + card) % 2 == 0:
            stack.pop()
        else:
            stack.append(card)
    return len(stack)

n = int(input())
input_string = input()
cards = list(map(int, input_string.split()))

remaining_cards = even(cards)
print(remaining_cards)
