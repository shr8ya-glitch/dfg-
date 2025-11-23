n=int(input("number"))
s=0
t=n
while t>0:
    d=t%10
    s=s+d**3
    t//=10
if n==s:
    print("Armstrong")
else:
    print("Not Armstrong")
m=int(input("enter the number"))
c=0
while m>0:
    m//=10
    c=c+1
print(c)