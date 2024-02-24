N = int(input())
arr = sorted(int(input()) for i in range(N))
ans = []
for i in arr:
    ans.append(i*N)
    N -= 1
print(max(ans))