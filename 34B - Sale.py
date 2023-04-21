_, m = map(int, input().split())

prices = sorted(list(map(int, input().split())))[:m]
ans = sum(i for i in prices if i<=0)
print(ans*-1)

