import sys
n = int(sys.stdin.readline())
def prime(x):
    if x<2:
        return False
    for i in range(2,int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

for _ in range(n):
    a = int(sys.stdin.readline())
    while True:
        if prime(a):
            print(a)
            break
        else:
            a += 1
