N = int(input())
arr = [[0]*1001 for _ in range(1001)]
for tc in range(1, N+1):
    i,j, w,h = map(int, input().split())
    for r in range(j,j+h):
            arr[r][i:i+w] = [tc]*w

for tc in range(1,N+1):
    print(sum([i.count(tc) for i in arr]))