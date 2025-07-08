# cafe menu

menu = {
    "pizza": 16.99,
    "burger": 12.99,
    "wings": 18.99,
    "fries": 5.99,
    "friesLrg": 8.99,
    "coke": 2.99,
    "water": 1.99,
}

print("** WELCOME TO MY CAFE **")
print("Here is our menu:")
for item, price in menu.items():
    print(f"{item} : ${price}")

bill_total = 0

while True:
    item = input("\nWhat would you like to order?\n")
    if item in menu:
        bill_total += menu[item]
        print(f"*{item}* has been added to your order.")
    else:
        print(f"SORRY! *{item}* is not available.")

    another = input("Do you want to order anything else? (yes/no)\n").lower()
    if another != "yes":
        break

print(f"\nYOUR TOTAL = ${bill_total:.2f}")


