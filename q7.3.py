l=list(map(int,input().split()))
even_count=0
odd_count=0
for i in range (0,len(l)):
    if (l[i]%2==0):
        even_count+=1
    else:
        odd_count+=1
print(even_count)
print(odd_count)