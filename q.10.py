# print the elements in a particular element in cyclic
k=int(input())
my_list=list(map(int,input().split(" ")))
n=len(my_list)
num=(k%n)
print(my_list[num])