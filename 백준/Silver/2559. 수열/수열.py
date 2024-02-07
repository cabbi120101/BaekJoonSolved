N, K = map(int, input().split())
arr = list(map(int, input().split()))

sum_temp = sum(arr[:K])
max_temp = sum_temp
for i in range(N-K):
    sum_temp += arr[i+K] - arr[i]
    if sum_temp > max_temp:
        max_temp = sum_temp
print(max_temp)