N = int(input())
arr = list(map(int, input().split()))
ans = 0
for i in arr:
    if i > 1:
        flag = True
        for j in range(2, int(i**(0.5))+1):
            if i % j == 0:
                flag = False
                break
        if flag:
            ans += 1
print(ans)