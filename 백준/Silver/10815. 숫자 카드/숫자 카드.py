import sys
N = int(sys.stdin.readline())
N_list = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
M_list = list(map(int, sys.stdin.readline().split()))
ans = {}
for i in range(len(N_list)):
    ans[N_list[i]] = 0

for j in range(M):
    if M_list[j] not in ans:
        print(0, end=' ')
    else:
        print(1, end=' ')