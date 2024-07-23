li=list(map(int,input().split()))
sum=0
avg=0
count=0
for i in range(0,len(li)):
    if(i%2==0):
       sum+=li[i]
       count+=1
       avg=sum/count
print(avg)