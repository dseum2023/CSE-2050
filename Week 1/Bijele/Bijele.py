## Author: Daniella Seum, dseum2023@my.fit.edu
## Course: CSE 2050, Fall 2024
## Project: Bijele, week 1, problem E

def num_pieces(a, b, c, d, e, f):
    a = 1-a
    b = 1-b
    c = 2-c
    d = 2-d
    e = 2-e
    f = 8-f
    return a, b, c, d, e, f


king, queen, rook, bishop, knight, pawn = map(int, input().split())
a, b, c, d, e, f = num_pieces(king, queen, rook, bishop, knight, pawn)
print(a, b, c, d, e, f)
