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
    
    for i in range(2, num // 2 + 1):
        if primes[i] and primes[num - i]:
            cnt += 1
                
    print(cnt)