n, d = map(int, input().split())
 
times = list(map(int, input().split()))
 
if sum(times)+ (10*(n-1))>d:
    print(-1)
else:
    d-= sum(times)
    print(d//5)
