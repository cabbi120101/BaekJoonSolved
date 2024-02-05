import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
h_list = []
for _ in range(n):
    h_list.append(int(input()))
h_list = [(x,0) for x in h_list]
h_q = deque()
h_q.extend(h_list) #누적합,값을 h_q라는 덱에 담는다

tmp_stack = []
ans = 0
while h_q: #덱의 오른쪽부터 pop하며 tmp_stack에 push한다. tmp_stack의 가장 위의 값이 x보다 작은동안, 즉 옥상정원을 볼 수 있는만큼 stack 값을 pop한다. 
    x,summed = h_q.pop()
    cnt_pop = 0
    while tmp_stack and tmp_stack[-1][0]<x:
        x2,summed2 = tmp_stack.pop()
        cnt_pop += summed2+1 #cnt_pop에 누적합+1만큼 증가시킨다. (해당 값이 이전에 pop해온 개수 + 1만큼 옥상정원을 볼 수 있음)
    ans+=cnt_pop
    tmp_stack.append((x,cnt_pop))
print(ans)