a, A = map(int,input().split())
b, B = map(int,input().split())
A1,B1 = A,B

g1 = a*B + b*A
g2 = A*B

G1,G2 = g1,g2

while G1%G2 != 0 :
    G1,G2 = G2,G1%G2

print(g1//G2, g2//G2)