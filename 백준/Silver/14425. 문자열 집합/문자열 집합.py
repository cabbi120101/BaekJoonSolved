import sys
N,M = map(int, sys.stdin.readline().split())
N_list = list(str(sys.stdin.readline()) for _ in range(N)) 
M_list = list(str(sys.stdin.readline()) for _ in range(M))
ans = {}
check = 0
for i in range(N):
    ans[N_list[i]] = 0
for j in range(M):
    if M_list[j] in ans:
        check += 1
print(check)