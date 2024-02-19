def chk_max_len(arr):
    max_len = 0
    for i in range(1, len(arr)):
        temp_len = arr[i] - arr[i-1]
        if temp_len > max_len:
            max_len = temp_len
    return max_len
def Qsort_list(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    L, P, R = [], [], []
    for num in arr:
        if num < pivot:
            L.append(num)
        elif num > pivot:
            R.append(num)
        else:
            P.append(num)
    return Qsort_list(L) + P + Qsort_list(R)

G, S = map(int, input().split())
N = int(input())
G_list = []
S_list = []

for _ in range(N):
    gs, num = map(int, input().split())
    if gs == 0:
        G_list.append(num)
    else:
        S_list.append(num)

G_list = [0] + Qsort_list(G_list) + [S]
S_list = [0] + Qsort_list(S_list) + [G]

print(chk_max_len(G_list)*chk_max_len(S_list))