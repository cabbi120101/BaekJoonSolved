N,K = map(int, input().split())
from collections import deque
def bfs():
    visited = [-1]*(100001)
    visited[N] = 0
    stack = deque([N])

    while stack:
        node = stack.popleft()

        if node == K:
            return visited[node]
        if 0 <= node - 1 < 100001 and visited[node - 1] == -1:
            visited[node - 1] = visited[node] + 1
            stack.append(node - 1)
        if 0 < node * 2 < 100001 and visited[node * 2] == -1:
            visited[node * 2] = visited[node]
            stack.appendleft(node * 2)
        if 0 <= node + 1 < 100001 and visited[node + 1] == -1:
            visited[node + 1] = visited[node] + 1
            stack.append(node + 1)

        # for move in [node*2, node-1, node+1]:
        #     if 0<=move<100001 and visited[move] == -1:
        #         if move == node*2 and move != 0:
        #             visited[move] = visited[node]
        #             stack.appendleft(move)
        #         else:
        #             visited[move] = visited[node]+1
        #             stack.append(move)
print(bfs())