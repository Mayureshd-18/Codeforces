s = input()
 
while "144" in s:
    s = s.replace("144","x")
    
while "14" in s:
    s = s.replace("14","x")
 
while "1" in s:
    s = s.replace("1","x")
    
if len(set(s))==1 and s[0]=="x":
    print("YES")
else:
    print("NO")
