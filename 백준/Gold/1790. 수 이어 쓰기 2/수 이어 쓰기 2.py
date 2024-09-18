N, k = map(int, input().split())

length = 0  # 현재까지 본 자리수의 총 길이
digit = 1   # 자리수
start = 1   # 해당 자리수에서의 시작 숫자

while True:
    # 현재 자리수에서의 숫자의 개수
    num_count = 9 * start
    # 해당 자리수에서 차지하는 자리수의 총합
    count = num_count * digit

    if k <= length + count: 
        break

    length += count 
    start *= 10 
    digit += 1 

# k번째 자리가 포함된 숫자 계산
num_index = (k - length - 1) // digit 
num = start + num_index 

# 숫자가 N을 초과할 수 있으므로 확인
if num > N:
    print(-1)
else:
    digit_index = (k - length - 1) % digit
    print(str(num)[digit_index]) 