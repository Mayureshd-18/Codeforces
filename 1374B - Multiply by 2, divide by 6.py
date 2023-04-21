for _ in range(int(input())):
    n = int(input())
    res = 0
    while n !=1:
        if n%3!=0:
            res = -1
            break
        if n%6==0:
            n//=6
        else:
            n*=2
        res+=1
        # print(n)
    print(res)
