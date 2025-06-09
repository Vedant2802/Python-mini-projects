
# example 1

# name = input("enter your name: ")

# while name == "":
#     print("you did not enter your name")
#     name = input("enter your name: ")
# print(f"Hello {name}")

# example 2

food = input("enter the food you like: (q to quit)")

while not food == "q":
    print(f"you like {food}")
    food = input("enter the food you like: (q to quit)")

print(f"bye")