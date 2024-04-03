N = int(input())
score = list(map(int, input().split()))
M = max(score)

result = 0
for i in range(N):
    score[i] = (score[i] / M) * 100
    result += score[i]

result = result / N
print(result)