## Author: Daniella Seum, dseum2023@my.fit.edu
## Course: CSE 2050, Fall 2024
## Project: Square Deal, week 6, problem A

def square_deal(rectangles):
    rotations = []
    
    for w, h in rectangles:
        rotations.append([(w, h), (h, w)])
        
    for r0 in [0, 1]:
        for r1 in [0, 1]:
            for r2 in [0, 1]:
                
                orientation = [
                    rotations[0][r0],
                    rotations[1][r1],
                    rotations[2][r2],
                ]
                
                (w1, h1), (w2, h2), (w3, h3) = orientation
                
                if w1 == w2 == w3:
                    total_height = h1 + h2 + h3
                    if total_height == w1:
                        return "YES"
                        
                if h1 == h2 == h3:
                    total_width = w1 + w2 + w3
                    if total_width == h1:
                        return "YES"
                      
                if w1 == w2:
                    square_height = h1 + h2
                    if square_height == h3 and w1 + w3 == square_height:
                        return "YES"
                      
                if w1 == w3:
                    square_height = h1 + h3
                    if square_height == h2 and w1 + w2 == square_height:
                        return "YES"
                       
                if w2 == w3:
                    square_height = h2 + h3
                    if square_height == h1 and w2 + w1 == square_height:
                        return "YES"
                       
                if h1 == h2:
                    square_width = w1 + w2
                    if square_width == h3 and h1 + h3 == square_width:
                        return "YES"
                        
                if h1 == h3:
                    square_width = w1 + w3
                    if square_width == h2 and h1 + h2 == square_width:
                        return "YES"
                        
                if h2 == h3:
                    square_width = w2 + w3
                    if square_width == w1 and h2 + h1 == square_width:
                        return "YES"
                        
    return "NO"
    

rectangles = []
for i in range(3):
    w, h = map(int, input().split())
    rectangles.append((w, h))

print(square_deal(rectangles))
