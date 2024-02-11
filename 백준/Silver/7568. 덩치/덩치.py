N = int(input())
student_list = [tuple(map(int, input().split())) for _ in range(N)]

for i in student_list:
    rank = 1
    for j in student_list:
        if i[0] < j[0] and i[1] < j[1]:
                rank += 1
    print(rank, end = " ")