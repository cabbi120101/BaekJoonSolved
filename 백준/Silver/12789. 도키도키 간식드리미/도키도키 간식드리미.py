n = int(input())
standing = list(map(int, input().split()))
stack = []
target = 1
 
while standing:
    if standing[0] == target:
        target += 1
        standing.pop(0)
    else:
        stack.append(standing.pop(0))
 
    while stack:
        if stack[-1] == target:
            stack.pop()
            target += 1
        else:
            break
print('Sad' if stack else 'Nice')