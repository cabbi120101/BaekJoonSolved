N = int(input())
arr = list(map(int, input().split()))
ans1 = [1]*N
ans2 = [1]*N
for i in range(N-1):
    if arr[i+1] >= arr[i]:
        ans1[i+1] += ans1[i]

    if arr[i+1] <= arr[i]:
        ans2[i+1] += ans2[i]

print(max(max(ans1),max(ans2)))