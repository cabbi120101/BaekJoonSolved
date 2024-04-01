while True:
    n = input()
    n2 = n[::-1]
    if n == '0':
        break
    elif n == n2:
        print('yes')
    else:
        print('no')