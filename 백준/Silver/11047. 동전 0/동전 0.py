N, K = map(int, input().split())
ans = 0
M_list = [int(input()) for _ in range(N)]

for coin in M_list[::-1]:
    if K >= coin:
        ans += K // coin
        K %= coin
        if K <= 0:
            break
print(ans)