N, k = map(int,input().split())
Y = sorted(list(map(int, input().split())))[::-1]
print(Y[:k][-1])