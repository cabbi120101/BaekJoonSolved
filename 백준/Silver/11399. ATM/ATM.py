N = int(input())
person  = list(map(int, input().split()))

def merge_sort(x):
    if len(x) <= 1:
        return x
    left = merge_sort(x[:len(x)//2])
    right = merge_sort(x[len(x)//2: ])
    i,j,k = 0,0,0
    while i<len(left) and j<len(right):
        if left[i] < right[j]:
            x[k] = left[i]
            i += 1
        else:
            x[k] = right[j]
            j += 1
        k += 1
    if i == len(left):
        while j < len(right):
            x[k] = right[j]
            j += 1
            k += 1
    elif j == len(right):
        while i < len(left):
            x[k] = left[i]
            i += 1
            k += 1
    return x


ans = 0
sort_person = merge_sort(person)
for i in range(N):
    ans += sort_person[i] * (N-i)
print(ans)