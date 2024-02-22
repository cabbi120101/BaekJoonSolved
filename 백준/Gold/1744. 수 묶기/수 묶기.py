N = int(input())
pos = []
nega = []
ans = 0
for i in range(N):
    num = int(input())
    if num <= 0:
        nega.append(num)
    elif num == 1:
        ans += 1
    else:
        pos.append(num)

pos = sorted(pos, reverse=True)
nega.sort()
def chk_sum(arr):
    res = 0
    for i in range(0, len(arr), 2):
        if i+1 < len(arr):
            res += arr[i]*arr[i+1]
        else:
            res += arr[i]
    return res

ans += chk_sum(pos) + chk_sum(nega)
print(ans)