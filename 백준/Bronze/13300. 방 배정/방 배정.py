N, K = map(int, input().split())
arr = [tuple(map(int, input().split())) for _ in range(N)]
ans = len(set(arr))
limit = 0

while arr:
    for i in set(arr):
        arr.pop(arr.index(i))
    limit += 1
    if limit == K:
        K = 0
        ans += 1
print(ans)