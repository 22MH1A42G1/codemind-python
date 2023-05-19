l = int(input())
r = int(input())
res = [i for i in range(l, r+1) if '0' not in str(i) and all(i % int(d) == 0 for d in str(i))]
print(' '.join(map(str, res)))
