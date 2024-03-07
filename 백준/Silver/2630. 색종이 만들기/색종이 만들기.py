N = int(input())
arr1 = [list(map(int, input().split())) for _ in range(N)]
zero = 0
one = 0
def chk(arr):
    global one
    global zero
    num = len(arr)
    sum_arr = sum([sum(i) for i in arr])
    if sum_arr == 0 :
        zero += 1
    elif sum_arr == num*num:
        one += 1
    else:
        chk([i[num//2:] for i in arr[num//2:]])
        chk([i[num//2:] for i in arr[:num//2]])
        chk([i[:num//2] for i in arr[num//2:]])
        chk([i[:num//2] for i in arr[:num//2]])
chk(arr1)
print(zero)
print(one)