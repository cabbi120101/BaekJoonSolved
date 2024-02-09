N = int(input())
N_ls = sorted(list(map(int, input().split())))
M = int(input())
M_ls = list(map(int, input().split()))

def binary(target, ls, start, end):
    if start > end:
        return 0
    m = (start+end)//2
    if target == ls[m]:
        return 1
    elif target < ls[m]:
        return binary(target, ls, start, m-1)
    else:
        return binary(target, ls, m+1, end)
for target in M_ls:
    start = 0
    end = N-1
    print(binary(target, N_ls, start, end))