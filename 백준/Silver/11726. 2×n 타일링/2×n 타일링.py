N = int(input())
arr = [0]*1001
arr[0] = 1
arr[1] = 2
if N >=2:
    for i in range(2,N):
        arr[i] = arr[i-2] + arr[i-1]
print(arr[N-1]%10007)