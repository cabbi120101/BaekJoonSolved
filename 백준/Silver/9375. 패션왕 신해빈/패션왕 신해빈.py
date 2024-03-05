T = int(input())
for tc in range(1,T+1):
    n = int(input())
    closet = dict()
    for _ in range(n):
        v, key = input().split()
        closet[key] = closet.get(key, []) + [v]
    ans = 1
    for i in closet:
        ans *= (len(closet[i])+1)
    print(ans-1)