for _ in range(int(input())):
    n, t = map(int, input().split())
    duration = list(map(int, input().split()))
    enter = list(map(int, input().split()))
 
    max_idx = -1
    max_entr = 0
 
    for i in range(len(duration)):
        if duration[i] + i <= t and enter[i] > max_entr:
            max_idx = i+1
            max_entr = enter[i]
 
    print(max_idx)
