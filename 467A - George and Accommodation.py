res = 0
for _ in range(int(input())):
    p,q = map(int, input().split())
    if q-p>=2:res+=1
print(res)
