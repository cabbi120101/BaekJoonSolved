N = int(input())
name = []
for i in range(N):
    a,b = input().split()
    name.append([int(a),str(b)])
name.sort(key = lambda x:(x[0]))
for i in name:
    print(*i)