N, M = map(int, input().split())
def LEM(n,m):
    if n % m == 0:
        return m
    else:
        return LEM(m, n%m)
def GCD(n,m):
    return n*m//LEM(n,m)
print(LEM(N,M) if N > M else LEM(M,N))
print(GCD(N,M) if N>M else GCD(M,N))