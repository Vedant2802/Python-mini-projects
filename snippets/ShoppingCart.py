item = input("What item do you want to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many do you want?: "))
total = price * quantity
print(f"You haev bought {quantity} of {item}")
print(f"The total is {total}")  