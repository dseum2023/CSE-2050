## Author: Daniella Seum, dseum2023@my.fit.edu
## Course: CSE 2050, Fall 2024
## Project: Video Speedup, week 6, problem C

def og_time(p, k, timestamps):
    current_percent = 100
    current_time = 0
    times = []

    for i in timestamps:
        current_time_diff = i - current_time
        times.append(current_time_diff * (current_percent / 100))
        current_percent = current_percent + p
        current_time = i

    final_time_diff = k - current_time
    times.append(final_time_diff * (current_percent / 100))

    original_time = 0
    for time in times:
        original_time = original_time + time

    return original_time

n, p, k = map(int, input().split())

timestamps = []
timestamps = list(map(int, input().split()))

print(og_time(p, k, timestamps))
