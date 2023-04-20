n, m = map(int, input().split())
puzzles = sorted(list(map(int, input().split())))
min_diff = float('inf')
diff = 0
for a, _ in enumerate(range(m - n + 1 )):
    diff =  puzzles[n-1] - puzzles[a]
    min_diff = min(min_diff, diff)
#     print(diff)

    n+=1
min_diff = min(min_diff, diff)

print(min_diff)

