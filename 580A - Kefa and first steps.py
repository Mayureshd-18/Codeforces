int(input())
lst = list(map(int, input().split()))
result= 0
temp = 1
for i in range(1, len(lst)):
    if lst[i]>= lst[i-1]:
        temp+=1
    else:
        result = max(result, temp)
        temp= 1
    # print(temp, result, lst[i])
result = max(result, temp)
print(result)
