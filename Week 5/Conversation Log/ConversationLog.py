## Author: Daniella Seum, dseum2023@my.fit.edu
## Course: CSE 2050, Fall 2024
## Project: Conversation Log, week 5, problem C

def conversation_log_analysis():
    M = int(input())
    all_users = set()
    word_users = {}
    word_counts = {}

    for _ in range(M):
        line = input().strip()
        if not line:
            continue  # Skip empty lines
        parts = line.split()
        if not parts:
            continue  # Skip lines with no content
        user = parts[0]
        all_users.add(user)
        words = parts[1:]
        for word in words:
            if word not in word_users:
                word_users[word] = set()
            word_users[word].add(user)
            if word not in word_counts:
                word_counts[word] = 0
            word_counts[word] += 1

    common_words = []
    for word in word_users:
        if word_users[word] == all_users:
            common_words.append((-word_counts[word], word))

    if not common_words:
        print("ALL CLEAR")
    else:
        common_words.sort()
        for _, word in common_words:
            print(word)


conversation_log_analysis()
