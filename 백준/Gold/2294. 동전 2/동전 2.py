n,k = map(int, input().split())
coin_list =[int(input()) for _ in range(n)]
coin_list.sort()

dp = [1e9]*(k+1)
dp[0] = 0

for coin in coin_list:
    for i in range(coin, k + 1):
        if coin > i:
            break
        dp[i] = min(dp[i], dp[i - coin] + 1)

if dp[k] == 1e9:
    print(-1)
else:
    print(dp[k])