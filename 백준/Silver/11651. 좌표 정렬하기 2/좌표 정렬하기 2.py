import sys
N = int(sys.stdin.readline())
coor = []
for i in range(N):
    [a,b] = map(int, sys.stdin.readline().split())
    coor.append([a,b])
coor.sort(key = lambda x:(x[1], x[0]))
for i in coor:
    print(*i)