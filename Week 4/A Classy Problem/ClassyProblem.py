## Author: Daniella Seum, dseum2023@my.fit.edu
## Course: CSE 2050, Fall 2024
## Project: Classy Problem, week 4, problem D

T = int(input())
for _ in range(T):
    n = int(input())
    people = []
    max_depth = 0

    for _ in range(n):
        line = input().strip()
        name_part, class_part = line.split(': ')
        name = name_part
        class_levels_str = class_part[:-6] 
        class_levels = class_levels_str.split('-')
        class_levels.reverse()  
        max_depth = max(max_depth, len(class_levels))

        people.append({
            'name': name,
            'class_levels': class_levels
        })

    person_keys = []
    for person in people:
        levels = person['class_levels']
        mapped_levels = []
        for level in levels:
            if level == 'upper':
                mapped_levels.append(3)
            elif level == 'middle':
                mapped_levels.append(2)
            elif level == 'lower':
                mapped_levels.append(1)
        while len(mapped_levels) < max_depth:
            mapped_levels.append(2)
        inverted_levels = [-lvl for lvl in mapped_levels]
        person_keys.append((inverted_levels, person['name']))


    person_keys.sort()


    for key in person_keys:
        print(key[1])
    print('=' * 30)
