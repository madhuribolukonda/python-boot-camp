# replace elements in an array with average of max and min
my_list=list(map(int,input().split(" ")))
max=my_list[0]
for i in range(len(my_list)):
    if(my_list[i]>max):
        max=my_list[i]
print(max)
min=my_list[0]
for i in range(len(my_list)):
    if(my_list[i]<min):
        min=my_list[i]
print(min)
avg=(max+min)//2
print(avg)
for i in range(len(my_list)):
    my_list[i]=avg
print(my_list)