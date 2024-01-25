N,M = map(int, input().split())
eye = {str(input()) for i in range(N)}
ear = {str(input()) for j in range(M)}
ans = sorted(list(eye&ear))
print(len(ans))
for i in ans:
    print(i)