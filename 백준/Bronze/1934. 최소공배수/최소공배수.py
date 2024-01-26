import sys
T = int(sys.stdin.readline())
for i in range(T):
    a,b = map(int,sys.stdin.readline().split())
    A,B = a,b

    while a%b != 0 :
        a,b = b,a%b

    print(A*B//b)