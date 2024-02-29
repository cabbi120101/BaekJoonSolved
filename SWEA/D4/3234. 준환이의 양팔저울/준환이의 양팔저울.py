T = int(input())

def chk_w(idx,L,R):
    global ans
    if sum_w//2 < L:
        ans += 2**(N-idx)
        return
    if idx == N:
        ans += 1
        return
    chk_w(idx+1, L+choose[idx], R)
    if L >= R + choose[idx]:
        chk_w(idx+1, L, R + choose[idx])

from itertools import permutations
for tc in range(1, T+1):
    N = int(input())
    w = list(map(int, input().split()))
    ans = 0
    sum_w = sum(w)
    for i in permutations(w, N):
        choose = i
        chk_w(0,0,0)
    print(f'#{tc} {ans}')