n = input()
n = list(n)
s = set(n)
if len(n)==len(s):
    print("Unique Number")
else:
    print("Not Unique Number")