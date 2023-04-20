n, m = map(int, input().split(" "))
if n % 2 == 0 and m <= n // 2 or n % 2 != 0 and m <= (n // 2) + 1:
    print(2*m-1)
elif n % 2 == 0:
    m-=n//2
    print(2*m)
else:
    m-=(n//2)
    print(2* (m - 1))
