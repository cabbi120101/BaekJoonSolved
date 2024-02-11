T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    temp = 0
    flag = False
    ans = 0
    while arr:

        if temp == M:
            flag = True
        else:
            temp += 1

        if arr[0] >= max(arr[0:]):
            arr.pop(0)
            ans += 1
            if flag:
                break
        else:
            arr.append(arr.pop(0))
            if flag:
                M = len(arr) - 1
                flag = False
                temp = 0
    print(ans)