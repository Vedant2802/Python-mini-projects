# program1

age = int(input("Enter your age: " ))
day = str(input("Enter the day: "))

price = 12 if age >= 18 else 8

if day.islower() or day.isupper():
    price = price-2

print(f"Ticket price for you is {price}")

# program 2



