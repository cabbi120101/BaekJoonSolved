T = int(input())
for t in range(T):
    N = int(input())
    ls = list(map(int, input().split()))
    mx = max(ls)
    d = {
        1: 0,
        2: 0,
    }
    for i in ls:
        d[2] += (mx-i)//2
        d[1] += (mx-i) % 2
    
    minv = float('inf')
    for i in range(d[2]+1):
        ones = (d[2]-i)*2 + d[1]
        temp = max(i*2, ones*2-1)
        if minv > temp:
            minv = temp
    print(f'#{t+1}',minv)