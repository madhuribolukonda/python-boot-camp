#patterns
m=int(input())
for i in range(m):
    for j in range(m):
        if(i==j):
            print("$",end="")
        else:
            print("*",end="")
    print()