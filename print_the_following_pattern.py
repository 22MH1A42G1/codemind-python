N = int(input())
for i in range(N):
    for j in range(N):
        if not(i == j):
            print('x', end='')
        else:
            print('0', end='')
    print()