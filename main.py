n=int(input("Enter the number"))
s=0
for i in range(1,n+1):
    s=s+i
    print(s)

m=input("Enter name")
r=('')
for i in m:      
    r=i+r

print("original name=",n)
print("reversed name=",r)

a=int(input("Enter the number"))
print("formatted:".format(n,1))
for i in range(n,0,-1):
    print(i)

base=2
e=3
r=base**e
print(r)