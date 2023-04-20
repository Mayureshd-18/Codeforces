s = input()
s = s.split("WUB")
 
res = [ele for ele in s if not ele.isspace()]
 
ans = " ".join(res)
print(ans.strip())
