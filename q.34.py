m=input()
count=0
ans=""
for i in m:
    if(i=="-"):
        count+=1
    else:
        ans=ans+i
print("-"*count+ans)