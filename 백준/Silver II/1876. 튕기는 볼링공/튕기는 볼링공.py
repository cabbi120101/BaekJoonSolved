import math
t = int(input())
for tc in range(1,t+1):
    T, X = map(float, input().split())
    rail = 0
    # sin에 radian으로 값을 입력해야함
    # a + b = 16/sin 볼링공과 핀 거리
    # a + b = 6/cos(pi/2-θ) + 10/cos(pi/2-θ) = 6/sinθ + 10/sinθ = 16/sinθ
    # 충돌시 최대 거리, 보다 작거나 같으면 충돌
    # T 미터라서 *100
    # 볼링 치는 두가지,,,
    # 앞에서 치는 것
    left = T * 100 - (16.0 / (math.sin(math.pi * X / 180)))
    # 뒤에서 치는 것
    right = T * 100 + (16.0 / (math.sin(math.pi * X / 180)))
    # 한번 옆에 부딪치고 중앙에 돌아오려면 같은 거리만큼 추가해야하므로 *2함
    step = (105/2 - 10)*2 / math.tan(math.pi * X / 180)
    while rail < right:
        # T - (a+b), T + (a+b) 사이에 값이 있으면 충돌
        if left < rail and rail < right:
            print('yes')
            break
        rail += step
        if rail >= right:
            print('no')