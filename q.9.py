# find the elements that is present in k+n index
my_list=list(map(int,input().split(" ")))
k=int(input())
n=int(input())
for i in range (0,len(my_list)):
     print(my_list[k+n],end=" ")
     break

