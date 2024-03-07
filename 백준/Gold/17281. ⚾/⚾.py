from itertools import permutations
import sys
N = int(sys.stdin.readline())
innings = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
ans = 0
for line in permutations(range(1,9),8):
    line = list(line[:3])+[0]+list(line[3:])
    hitter = 0
    res = 0
    for i in range(N):
        out = 0
        b1, b2, b3 = 0,0,0
        while out < 3:
            go = innings[i][line[hitter]]
            if go == 0:
                out += 1
            elif go == 1:
                res += b3
                b3,b2,b1 = b2,b1,1
            elif go == 2:
                res += b3 + b2
                b3,b2,b1 = b1,1,0
            elif go == 3:
                res += b3 + b2 + b1
                b3,b2,b1 = 1,0,0
            elif go == 4:
                res += b3 + b2 + b1 + 1
                b3,b2,b1 = 0,0,0
            hitter = (hitter+1) % 9
    if res > ans:
        ans = res
print(ans)