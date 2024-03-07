import sys
import heapq
input = sys.stdin.readline
N = int(input())
q = []
for _ in range(N):
    temp = int(input())
    if temp == 0:
        if not q:
            print(0)
        else:
            print(heapq.heappop(q))
    else:
        heapq.heappush(q, temp)