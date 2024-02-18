import sys
N, M  = map(int, input().split())
password = {}
for _ in range(N):
    site, word = sys.stdin.readline().split()
    password[site] = word
for _ in range(M):
    print(password[input()])