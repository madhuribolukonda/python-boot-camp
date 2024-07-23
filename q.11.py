#find the max element in a given list
my_list=list(map(int,input().split(" ")))
#print(max(my_list)
# for i in range (0,len(my_list),i+1):
# my_list(i)<my_list(i+1)
# print(i)
max=my_list[0]
for i in range(len(my_list)):
    if(my_list[i]>max):
        max=my_list[i]
print(max)