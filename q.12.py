# find min element in a listy_list=list(map(int,input().split(" ")))
#print(max(my_list)
# for i in range (0,len(my_list),i+1):
# my_list(i)<my_list(i+1)
# print(i)
my_list=list(map(int,input().split(" ")))
min=my_list[0]
for i in range(len(my_list)):
    if(my_list[i]<min):
        min=my_list[i]
print(min)