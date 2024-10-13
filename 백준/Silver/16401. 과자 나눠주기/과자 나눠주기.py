M, N = map(int, input().split())
snack = list(map(int, input().split()))
snack.sort()

def check(snack,M,length):
    temp = 0
    for i in snack:
        temp += i // length
    return temp >= M


def find_max(M,snack):
    L,R = 1, max(snack)
    ans = 0

    while L <= R:
        mid = (L+R)//2
        if check(snack,M,mid):
            ans = mid
            L = mid + 1
        else:
            R = mid - 1
    return ans

print(find_max(M,snack))