budget = int(input())
item_price = input()
total_spent = 0
while item_price != "End":
    total_spent += int(item_price)
    if total_spent > budget:
        print("You went in overdraft!")
        break
    item_price = input()

else:
    print("You bought everything needed.")