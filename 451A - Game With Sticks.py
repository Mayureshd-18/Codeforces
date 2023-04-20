m,n = map(int, input().split())
 
b = (m*n)//max(m,n)
 
if b%2==0:
    print("Malvika")
else:
    print("Akshat")
