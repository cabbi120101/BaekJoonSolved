T = int(input())
for tc in range(1, T+1):
    n = int(input())
    dp = [1,1,1]+[0]*(n-2)
    for i in range(3,n):
        dp[i] = dp[i-2] + dp[i-3]
    print(dp[n-1])