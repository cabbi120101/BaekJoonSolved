n = int(input())
A = list(map(int, input().split()))
X = int(input())
A.sort()
l,r = 0,n-1
ans = 0
while l < r:
    if A[l]+A[r] > X:
        r -= 1
    elif A[l]+A[r] == X:
        ans += 1
        l += 1
        r -= 1
    elif A[l]+A[r] < X:
        l += 1
print(ans)