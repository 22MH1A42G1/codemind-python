num = int(input())
c = 0
for i in range(num):
    if i * (i + 1) == num:
        c = 1
        break
if c == 1:
    print("YES")
else:
    print("NO")