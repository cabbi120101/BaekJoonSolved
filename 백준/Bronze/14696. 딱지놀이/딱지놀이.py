import sys

input = sys.stdin.readline

n = int(input())
score_dic = {1:0.0001,2:0.02,3:3,4:301} 
#각 라운드별로 최대 100개의 그림이 나올 수 있으므로, 
# 우선순위가 낮은 모양이 100개 나와도 다음 우선순위보다 값이 낮도록 딕셔너리 설정
for _ in range(n):
    a,*a_list = list(map(int,input().split()))
    b,*b_list = list(map(int,input().split()))
    a_score = 0
    b_score = 0
    for item in a_list:
        a_score+=score_dic[item]
    for item in b_list:
        b_score+=score_dic[item]
    if a_score>b_score:
        print('A')
    elif a_score<b_score:
        print('B')
    else:
        print('D')