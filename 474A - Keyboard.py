keys = "qwertyuiopasdfghjkl;zxcvbnm,./"

dirn = input()
s = input()
res = "".join(keys[keys.find(s[i]) - 1] if dirn == "R" else keys[keys.find(s[i]) + 1] for i in range(len(s)))

print(res)

