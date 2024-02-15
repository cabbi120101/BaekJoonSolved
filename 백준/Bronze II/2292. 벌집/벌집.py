N = int(input())
ans = 1
bee = 1
while N > bee:
    bee += 6*ans
    ans += 1
print(ans)