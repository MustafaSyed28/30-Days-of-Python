# cafe menu

menu= {
    "pizza" : 16.99,
    "burger" : 12.99,
    "wings" : 18.99,
    "fries" : 5.99,
    "friesLrg" : 8.99,
    "coke" : 2.99,
    "water" : 1.99,
}

print("** WELCOME TO MY CAFE **")
print("Here is our menu")
print("pizza : $16.99\nburger : $12.99\nwings : $18.99\nfries : $5.99\nfriesLrg : $8.99\ncoke : $2.99\nwater : $1.99")


bill_total = 0

item_1=input("What would you like to order?\n")
if item_1 in menu:
    bill_total  += menu[item_1]
    print(f"*{item_1}* has been added to your order")
else:
    print(f"SORRY! *{item_1}* is not available")

another_order= input("Do u want to order anything else? (yes/no)\n")

if another_order == "yes":
    item_2= input('What else whould you like to order?\n')
    if item_2 in menu:
        bill_total += menu[item_2]
        print(f"*{item_2}* has been added to your order")
    else:
        print(f"*{item_2}* is not available")


another_order1= input("Do u want to order anything else? (yes/no)\n")

if another_order1 == "yes":
    item_3= input('What else whould you like to order?\n')
    if item_3 in menu:
        bill_total += menu[item_3]
        print(f"*{item_3}* has been added to your order")
    else:
        print(f"*{item_3}* is not available")      


print(f"YOUR TOTAL = ${bill_total}")