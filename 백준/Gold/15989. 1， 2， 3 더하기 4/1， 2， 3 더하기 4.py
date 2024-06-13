T = int(input())
dp = [1]*(10001)
# dp[1] = 1
# dp[2] = 2
# dp[3] = 3
# dp[4] = 4
# dp[5] = 5
# dp[6] = 7
for i in range(2,10001):
    dp[i] += dp[i-2]
for i in range(3,10001):
    dp[i] += dp[i - 3]

for tc in range(1,T+1):
    n = int(input())
    print(dp[n])