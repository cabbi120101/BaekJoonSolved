T = int(input())
for tc in range(1,T+1):
    n = int(input())
    n_list = [0,1,2,4]+[0]*(n-3)
    for i in range(4,n+1):
        n_list[i] = n_list[i-1] + n_list[i-2] + n_list[i-3]
    print(n_list[n])