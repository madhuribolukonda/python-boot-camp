# remove all the brackets by given algebric expression
# m=input()
# check=("(",")")
# for i in m:
#     if (i not in check):
#         print(i,end="")

# by using ascii values
m=input()
for i in m:
    if(ord(i)==40 or ord(i)==41 or ord(i)==91 or ord(i)==93):
        pass
    else:
        print(i,end=" ")
print()        