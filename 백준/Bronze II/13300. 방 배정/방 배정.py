N, k = map(int, input().split())
student = [[0] * 7 for _ in range(3)] #성별 / 학년별

for _ in range(N):
    S, Y = map(int, input().split())
    student[S][Y] += 1
        
room = 0
for i in student:
    for j in i:
        if j%k != 0:
            room += (j // k)+1
        else:
            room += (j//k)

print(room)