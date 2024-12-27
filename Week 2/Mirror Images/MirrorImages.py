## Author: Daniella Seum, dseum2023@my.fit.edu
## Course: CSE 2050, Fall 2024
## Project: Mirror Images, week 2, problem F

def mirror_image(image, rows):
    return [row[::-1] for row in image[::-1]]

T = int(input())

for t in range(1, T + 1):
    R, C = map(int, input().split())
    image = [input() for _ in range(R)]
    mirrored_image = mirror_image(image, R)
    print(f"Test {t}")
    for row in mirrored_image:
        print(row)
