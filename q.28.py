# check how many vowels are there in a string
# m=input()
# check=['a','e','i','o','u']
# count=0
# for i in m:
#     if(i in check):
#         count+=1
# print(count)

# check how many vowels and consonents are there in a string
m=input()
inp=m.lower()
check=['a','e','i','o','u']
n="bcdfghjklmnpqrstvwxyz"
count=0
c=0
for i in inp:
    if(i in check):
        count+=1
print(count) 
for i in inp:
    if(i in n):
        c+=1
print(c)
