N = int(input())
for r in range(N):
    for c in range(1, N-2):
        print(c, end='')
    for c in range(N-2, 0, -1):
        print(c, end='')
    print()