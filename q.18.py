# find the sum of even no.of a digit in a given number
n=56789
sum=0
while n>0:
    r=n%10
    if(n%2==0):
       sum=sum+r
    n=n//10
print(sum)