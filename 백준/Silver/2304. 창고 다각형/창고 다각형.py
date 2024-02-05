N = int(input())
arr = [0]*1001
max_H = 0
max_idx = 0
for _  in range(N):
    L,H = map(int, input().split())
    arr[L] = H
    if max_H < H:
        max_idx = L
        max_H = H

ans = 0
tmp = 0
for i in range(max_idx+1):
    tmp = max(tmp, arr[i])
    ans += tmp

tmp2 = 0
for j in range(1000, max_idx, -1):
    tmp2 = max(tmp2, arr[j])
    ans += tmp2

print(ans)