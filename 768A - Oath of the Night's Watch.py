n = int(input())

lst = list(map(int, input().split()))
a = min(lst)
b = max(lst)
a1 = lst.count(a)
b1 = lst.count(b)
if n - a1-b1>0:
    print(n - a1 - b1)
else:
    print(0)
