N = int(input())
coor = []
for i in range(N):
    [a,b] = map(int, input().split())
    coor.append([a,b])
coor.sort()
for i in coor:
    print(*i)