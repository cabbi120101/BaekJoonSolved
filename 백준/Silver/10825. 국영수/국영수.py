import sys
N = int(input())
arr = [list(sys.stdin.readline().split()) for _ in range(N)]

sorted_arr = sorted(arr, key = lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for i in sorted_arr:
    print(i[0])