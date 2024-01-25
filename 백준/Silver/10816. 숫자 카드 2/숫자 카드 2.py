N = int(input())
N_list = list(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))
ans = {}
for i in N_list:
    if i in ans:
        ans[i] += 1
    else:
        ans[i] = 1

for j in M_list:
    if j in ans:
        print(ans[j], end=' ')
    else:
        print(0, end=' ')