def rp(s, i):
    return s[:i][::-1] + s[i:]


def os(n, k, s):
    o = list(s)
    for i in range(k, 0, -1):
        j = n - i
        o[:i] = rp(o, i)[:i]
    return ''.join(o)


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input().strip()
    o = os(n, k, s)
    print(o)