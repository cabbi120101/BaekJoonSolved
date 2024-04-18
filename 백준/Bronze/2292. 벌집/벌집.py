num = int(input())
numbox = 1
count = 1

while num > numbox:
    numbox += 6*count
    count += 1
print(count)