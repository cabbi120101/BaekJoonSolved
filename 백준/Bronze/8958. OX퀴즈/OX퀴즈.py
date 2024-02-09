T = int(input())
for tc in range(1,T+1):
    ls = input().split('X')
    ans = 0
    for i in ls:
        ans += (len(i)*(len(i)+1))//2
    print(ans)