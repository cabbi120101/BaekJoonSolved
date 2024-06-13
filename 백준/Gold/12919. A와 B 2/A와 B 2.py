S = list(input())
T = list(input())
ans = 0
def dfs(T):
    global ans
    if T == S:
        ans = 1
        return
    if len(T) == 0:
        return
    if len(S) > len(T):
        return
    if T[0] == 'B':
        dfs(T[1:][::-1])
    if T[-1] == 'A':
        dfs(T[:-1])
dfs(T)
print(ans)