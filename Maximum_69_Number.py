def max_69(self, num: int) -> int:
    return str(num).replace('6','9',1)
n=input()
print(max_69(1,n))