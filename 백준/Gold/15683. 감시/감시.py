N, M = map(int, input().split())
room = []
cctv = []
mode = [
    [],
    [[0],[1],[2],[3]],
    [[0,2], [1,3]],
    [[0,1],[1,2],[2,3],[0,3]],
    [[0,1,2],[0,1,3],[1,2,3],[0,2,3]],
    [[0,1,2,3]]]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

for i in range(N):
    line = list(map(int, input().split()))
    room.append(line)
    for j in range(M):
        if 0<line[j]<6:
            cctv.append([line[j],i,j])

def chk(arr, mode, y, x):
    for i in mode:
        ny = y
        nx = x
        while True:
            ny += dy[i]
            nx += dx[i]
            if ny < 0 or nx < 0 or ny >= N or nx >= M:
                break
            if arr[ny][nx] == 6:
                break
            elif arr[ny][nx] == 0:
                arr[ny][nx] = -1
def dfs(depth, arr):
    global min_v
    if depth == len(cctv):
        count = 0
        for i in range(N):
            count += arr[i].count(0)
        min_v = min(min_v, count)
        return

    test_room = [i.copy() for i in arr]
    cctv_num, y, x = cctv[depth]
    for i in mode[cctv_num]:
        chk(test_room, i, y, x)
        dfs(depth+1, test_room)
        test_room = [i.copy() for i in arr]

min_v = 1e9
dfs(0,room)
print(min_v)