arr = [[0]*101 for _ in range(101)]

for _ in range(4):
    x,y,x1,y1 = map(int, input().split())
    for i in range(y,y1):
        for j in range(x,x1):
            arr[i][j] = 1

print(sum(sum(i) for i in arr))