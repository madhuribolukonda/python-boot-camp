cost_apples=15
cost_bananas=4
cost_oranges=5
apples=int(input())
bananas =int(input())
oranges=int(input())

total=(cost_apples*apples + cost_bananas*bananas + cost_oranges*oranges)
print(total)
if(total < 700):
    print("shopkeeper is not cheater")
else:
    print("the shopkeeper is cheater")