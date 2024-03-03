T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    area = [list(map(int, input().split())) for _ in range(N)]
    house = [(i,j) for i in range(N) for j in range(N) if area[i][j] == 1]
    max_v = 0

    for k in range(1,N+2): # 마름모 사이즈 1~N+1까지
        for i in range(N):
            for j in range(N):
                home = 0 # 영역 안에 총 집 수
                for r, c in house: # 집리스트에서 하나씩 불러옴
                    # 중심(i,j) 보다 좌표 차 거리가 k 보다 작은 경우
                    # 영역(마름모)에 속한다.
                    # 크면 범위에 벗어남.
                    if abs(i-r) + abs(j-c) < k:
                        home += 1
                if home*M - (k*k+(k-1)*(k-1)) >= 0:
                    max_v = max(max_v, home)
    print(f'#{tc} {max_v}')