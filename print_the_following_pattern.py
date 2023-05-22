N = int(input())

for row in range(N):
    for col in range(N):
        if row == col or row + col == N - 1:
            print('x', end='')
        else:
            print('0', end='')
    print()
