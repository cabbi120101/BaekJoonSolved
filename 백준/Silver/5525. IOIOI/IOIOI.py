N = int(input())
M =  int(input())
S = input().strip()
def count_PN(N, M, S):
    count = 0
    i = 0
    pattern = 2 * N + 1  # 패턴 길이

    while i <= M - pattern:
        # 패턴의 시작 부분 확인
        if S[i] == 'I':
            # N번 반복하여 IOI 패턴 확인
            match = True
            for j in range(N):
                if S[i + 2 * j + 1] != 'O' or S[i + 2 * j + 2] != 'I':
                    match = False
                    break

            if match:
                count += 1
                # 중첩된 패턴 확인을 위해 두 칸 앞으로 이동
                i += 2
            else:
                # 패턴이 아니면 한 칸 앞으로 이동
                i += 1
        else:
            i += 1

    return count

print(count_PN(N, M, S))