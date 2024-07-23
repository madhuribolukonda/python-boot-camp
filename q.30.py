# print the unique charactritics in a string
m=input()
inp=m.lower()
ans=""
for i in inp:
    if (i not in ans):
        ans+=i
print(ans)