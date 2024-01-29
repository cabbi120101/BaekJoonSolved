import sys
t = int(sys.stdin.readline())
def prime_list(n):
    sieve = [True] * (n + 1)
    
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i] == True:
            
            for j in range(i + i, n + 1, i):
                sieve[j] = False     
    return sieve

nums = []

for _ in range(t):
    nums.append(int(sys.stdin.readline()))
    
max_num = max(nums)
primes = prime_list(max_num)

for num in nums:
    cnt = 0
    # 합이 num이 되는 i, num-i 값 모두 True(소수)일때를 구한다.
    # 두 수 합이 num이 되는 거니까 num//2의 값까지만 본다.
    for i in range(2, num // 2 + 1):
        if primes[i] and primes[num - i]:
            cnt += 1
                
    print(cnt)