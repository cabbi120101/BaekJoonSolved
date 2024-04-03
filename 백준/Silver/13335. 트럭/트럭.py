from collections import deque
N, W, L = map(int,input().split())  # N:트럭의 수 W:다리 길이 L:최대 하중
truck = list(map(int, input().split()))

# 큐의 자리는 W개 만큼 들어갈 수 있다.
# 덱을 사용하는게 편할듯??
# 덱 사용법이 기억이 하나도 안난다
# 넣고 빠질때 마다 카운트를 하나씩 세서 카운트를 출력하면 그게 최단시간이 될듯
# 덱이 빌때까지 반복하면 될듯
# 들어간데 10되면 안들어가고 빠질때까지
# 조건을 이리저리 걸면서 덱을 쓰면 될듯~~~~
# 덱이나 공부하고 오자
# q = deque()
# q.append(1)  # enqueue()
# t = q.popleft()  # dequeue()

truck_q = deque()

truck_q.append(truck[0])
count = 1
i = 0
while True:
    if i == int(N)-1:
        break
    # W개가 안차있을때
    if len(truck_q) != int(W):
        # W개 만큼 올라갈 수 있을 때
        if sum(truck_q) + truck[i+1] <= int(L):
            truck_q.append(truck[i+1])
            i += 1
        else:
            truck_q.append(0)
    # 이미 덱에 2개가 차있을때
    else:
        truck_q.popleft()  # 일단 뒤에 꺼 하나 빼고
        if sum(truck_q) + truck[i+1] <= int(L):
            truck_q.append(truck[i+1])
            i += 1
        else:
            truck_q.append(0)
    # 큐가 비었을 때 반복 멈추게 하는 것
    count += 1

count += W
print(count)