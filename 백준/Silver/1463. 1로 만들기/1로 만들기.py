N = int(input())
memo = [0] * (N+1)
memo[0] = 0
memo[1] = 0
for i in range(2,N+1):
    if i % 2 == 0 and i % 3 == 0:
        memo[i] = min(memo[i//2],memo[i//3],memo[i-1]) + 1
    elif i % 2 == 0:
        memo[i] = min(memo[i//2],memo[i-1]) + 1
    elif i % 3 == 0:
        memo[i] = min(memo[i//3],memo[i-1]) + 1
    else:
        memo[i] = memo[i-1] + 1

print(memo[N])