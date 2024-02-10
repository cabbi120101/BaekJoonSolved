K, N = map(int, input().split())

arr = [int(input()) for _ in range(K)]
start, end = 1, max(arr)

while end >= start:
    mid = (start + end) // 2
    res = sum([i // mid for i in arr])
    
    if res >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)