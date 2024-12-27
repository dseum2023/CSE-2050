## Author: Daniella Seum, dseum2023@my.fit.edu
## Course: CSE 2050, Fall 2024
## Project: Increasing Subsequence, Week 8, Problem B

def aaaaaaaaaaaaaaaah(a):##im tired
    n = len(a)
    dp = [1]*n ##init dp array with 1s
    seq = []  ##start with an empty list
    for _ in range(n):
        seq.append([])  
    for i in range(n):
        seq[i] = [a[i]] #start seq with current element
        for j in range(i):
            if a[j] < a[i]:
                if dp[j]+1 > dp[i]:
                    dp[i] = dp[j]+1 ##update
                    seq[i] = seq[j]+[a[i]] ##update
                elif dp[j]+1 == dp[i]:
                    tmp = seq[j]+[a[i]] ##same length handling
                    if tmp < seq[i]:
                        seq[i] = tmp
    m = max(dp)
    res = []
    for i in range(n):
        if dp[i] == m:
            res.append(seq[i]) ##collect all seqs
    res.sort()
    ans = res[0]
    return m, ans ##return length and sequence

while True:
    parts = input().split()
    N = int(parts[0])
    if N == 0:
        break ##exit once N is 0
    nums = []
    for i in range(1, N+1):
        nums.append(int(parts[i])) ##read sequence of nums
    ln, sub_seq = aaaaaaaaaaaaaaaah(nums)
    ln, sub_seq = aaaaaaaaaaaaaaaah(nums)
    res = str(ln)
    for n in sub_seq:
        res += ' ' + str(n) ##output in correct format
    print(res)
