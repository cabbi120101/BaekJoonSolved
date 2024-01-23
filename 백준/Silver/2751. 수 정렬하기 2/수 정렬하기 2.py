import sys
N = int(input())
N_list = [int(sys.stdin.readline()) for _ in range(N)]
for i in sorted(N_list):
    print(i)