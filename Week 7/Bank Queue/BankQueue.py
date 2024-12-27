## Author: Daniella Seum, dseum2023@my.fit.edu
## Course: CSE 2050, Fall 2024
## Project: bank queue, week 7, problem E

def mr_krabs(ppl, N, T):
    for _ in range(N):
        c_i, t_i  = map(int,input().split())
        ppl.append((c_i,t_i))
    
    ppl.sort(reverse=True)

    times=[0]*T
    total=0

    for c_i,t_i in ppl:
        time = t_i
 
        while time>=0:
     
            if times[time] ==0:
                times[time] = 1
                total += c_i
                break
            else:
                time-=1

    return(total)


N,T=map(int,input().split())
ppl=[]

print(mr_krabs(ppl, N, T))
