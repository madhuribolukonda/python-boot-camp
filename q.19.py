# reverse a number
n=123
# sum=0
# while n>0:
#     r=n%10
#     sum=sum*10+r
#     n=n//10
# print(sum)
rev=""
while n>0:
    r=n%10
    rev=rev+str(r)
    n=n//10
ans=int(rev)
print(ans)
print(type(ans))