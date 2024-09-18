import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.read

data = input().splitlines()
N = int(data[0])
tree = [[] for _ in range(N + 1)]
for line in data[1:]:
    u, v = map(int, line.split())
    tree[u].append(v)
    tree[v].append(u)

dp = [[0, 0] for _ in range(N + 1)] 
def dfs(node, parent):
    dp[node][0] = 0 
    dp[node][1] = 1  

    for child in tree[node]:
        if child != parent:
            dfs(child, node)
            dp[node][0] += dp[child][1]  
            dp[node][1] += min(dp[child][0], dp[child][1]) 
dfs(1, -1)

print(min(dp[1][0], dp[1][1]))