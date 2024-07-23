#for i in range(32,128):
#     print(chr(i),end=" ")
# print sum by ascii values  
# m=input()
# sum=0
# for i in m:
#     if (ord(i)>=48 and ord(i)<=57):
#         sum+=int(i)
# print(sum)

# write a program to print all the capitla letters in a string
m=input()
ans=" "
for i in m:
    if (ord(i)>=65 and ord(i)<=90):
       ans+=i
print(ans)