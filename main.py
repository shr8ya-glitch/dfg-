s=input("word::")
chr=input("character:")
i=0
c=0
while (i<len(s)):
    if s[i]==chr:
        c=c+1
    i=i+1
print("repeated:",c)