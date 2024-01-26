M, N = map(int, input().split())
def prime(x):
    if x<2:
        return False
    for i in range(2,int(x**0.5)+1):
        if x % i == 0:
            return False
    return True
for i in range(M,N+1):
    if prime(i):
        print(i)