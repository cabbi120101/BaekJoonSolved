import sys
from collections import  deque
def bfs(start):
    stack = deque([start])
    while stack:
        node = stack.popleft()
        if visited[node] == 0:
            visited[node] = 1
            stack.extend(tree[node])
N, M = map(int, sys.stdin.readline().split())
tree = dict()
for _ in range(M): # 트리 생성
    u,v = map(int, sys.stdin.readline().split())
    if u in tree:
        tree[u].append(v)
    else:
        tree[u] = [v]
    if v in tree:
        tree[v].append(u)
    else:
        tree[v] = [u]
visited = [0]*(N+1) # 방문
ans = 0 # 그룹 가지수

for i in range(1,N+1):
    if i not in tree:
        ans += 1
    elif visited[i] == 0: # 방문 안했다면
        bfs(i)
        ans += 1
print(ans)