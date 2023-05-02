for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    if len(arr)==2:
        print(arr[0]*arr[1])
    else:


        min1 = min(arr)
        arr.remove(min1)
        min2 = min(arr)
        # arr.remove(min2)

        c1 = min1*min2

        max1 = max(arr)
        arr.remove(max1)
        max2 = max(arr)

        c2 = max1*max2

        print(max(c1, c2))

