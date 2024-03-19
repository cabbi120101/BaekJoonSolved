import sys
N,K = map(int, input().split())
bag = [[0,0]]+[list(map(int, sys.stdin.readline().split())) for _ in range(N)]
ans = 0
dp = [[0]*(K+1) for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,K+1):
        weight = bag[i][0]
        value = bag[i][1]
        if j < weight:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j-weight] + value, dp[i-1][j])
print(dp[-1][-1])