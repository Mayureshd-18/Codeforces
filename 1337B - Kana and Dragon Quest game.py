for _ in range(int(input())):
    x,n,m = map(int, input().split())

    if x<=m*10:
        print("YES")
    else:
        while n > 0 and not (x // 2) + 10 >= x:
            x = x//2 + 10
            n-=1
        if x<=m*10:
            print("YES")
        else:
            print("NO")
