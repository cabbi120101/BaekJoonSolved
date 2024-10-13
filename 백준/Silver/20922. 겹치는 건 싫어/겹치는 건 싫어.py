N, K = map(int, input().split())
arr = list(map(int, input().split()))

def find_sub(N,K,arr):
    temp = {}
    L = 0
    max_len = 0

    for R in range(N):
        num = arr[R]
        if num in temp:
            temp[num] += 1
        else:
            temp[num] = 1

        while temp[num] > K:
            temp[arr[L]] -= 1
            if temp[arr[L]] == 0:
                del temp[arr[L]]
            L += 1
        
        max_len = max(max_len, R-L+1)

    return max_len


print(find_sub(N,K,arr))