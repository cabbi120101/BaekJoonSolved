import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
arr = list(map(int,input().split()))

for i in range(N-1):
    arr[i+1] += arr[i]
arr = [0] + arr
for _ in range(M):
    i,j = map(int,input().split())
    print(arr[j]-arr[i-1])