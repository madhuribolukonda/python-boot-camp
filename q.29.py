# write a program to print vowels and consonents
m=input()
inp=m.lower()
vowels="aeiou"
consonents="b,c,d,f,g,h,j,k,l,m,n,p,q,r,s,t,v,w,x,y,z"
ans=""
ans2=""
for i in inp:
    if(i in vowels):
        ans+=i
print(ans) 
for i in inp:
    if(i in consonents):
        ans2+=i
print(ans2)
