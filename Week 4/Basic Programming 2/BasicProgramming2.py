## Author: Daniella Seum, dseum2023@my.fit.edu
## Course: CSE 2050, Fall 2024
## Project: Basic Programming 2, week 4, problem C

N, t = map(int, input().split())
A = list(map(int, input().split()))

if t == 1:
    freq = {}
    found = False
    setA = set(A)
    from collections import Counter
    freq = Counter(A)
    for a in setA:
        b = 7777 - a
        if b in setA:
            if a != b:
                print("Yes")
                found = True
                break
            elif freq[a] >= 2:
                print("Yes")
                found = True
                break
    if not found:
        print("No")
elif t == 2:
    if len(set(A)) == N:
        print("Unique")
    else:
        print("Contains duplicate")
elif t == 3:
    from collections import Counter
    freq = Counter(A)
    found = False
    for num, count in freq.items():
        if count > N // 2:
            print(num)
            found = True
            break
    if not found:
        print(-1)
elif t == 4:
    A.sort()
    if N % 2 == 1:
        median = A[N // 2]
        print(median)
    else:
        median1 = A[N // 2 -1]
        median2 = A[N // 2]
        print(f"{median1} {median2}")
elif t ==5:
    filtered = [x for x in A if 100 <= x <= 999]
    filtered.sort()
    print(' '.join(map(str, filtered)))
