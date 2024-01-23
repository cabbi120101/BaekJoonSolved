N = int(input())
alp = []
for _ in range(N):
    i = str(input())
    alp.append(i)
alp = list(set(alp))
alp.sort(key = lambda x:(len(x), x))
for i in alp:
    print(i)