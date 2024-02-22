M = int(input())
end = M*5
start = 5
ans = -1
def chk_5(n):
    res = 0
    while n >= 5:
        n //= 5
        res += n
    return res

while start <= end:
    mid = (start+end)//2
    temp = chk_5(mid)
    if temp < M:
        start = mid + 1
    else:
        end = mid - 1
        ans = mid
    

print(ans if M == chk_5(ans) else -1)