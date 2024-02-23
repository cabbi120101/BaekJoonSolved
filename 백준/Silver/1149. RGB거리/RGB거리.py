N = int(input())
arr = [list(map(int, input().split())) for i in range(N)]
def chk_min(chk_arr):
    min_v = 1e9
    for i in chk_arr:
        if i < min_v:
            min_v = i
    return min_v
for i in range(1,N):
    arr[i][0] = chk_min([arr[i - 1][1], arr[i - 1][2]]) + arr[i][0]
    arr[i][1] = chk_min([arr[i - 1][0], arr[i - 1][2]]) + arr[i][1]
    arr[i][2] = chk_min([arr[i - 1][0], arr[i - 1][1]]) + arr[i][2]
print(chk_min(arr[N-1]))
