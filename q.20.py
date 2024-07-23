#  mr.x is trying to create a new password for instagram account.these are the required conditions for creating a new password the conditions are 
# 1.minimum length is 8 and maximum length is 15
# 2.only @ and / are allowed
# 3.no spaces are allowed
# 4.only alpha numeris are allowed
# you are supposed to enter 
# weak if length is exact 8
# medium if length is between 8-12
# strong if length is between 12-15
#my_list=str(map(int,input().split("")))
string=input()
m=len(string)
if (m>=8 and m<=15):
#if (only  are present):
#if (""):
    print("your password is corret")
else:
    print("your password s incorrect")