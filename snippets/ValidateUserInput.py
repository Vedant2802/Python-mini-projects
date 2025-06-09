# validate user inout exercise
# 1. username has no more than 12 char
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("Enter your username: ")

if len(username) > 12:
    print("username can not have more than 12 characters")

elif not username.find(" ") == -1:
    print("username can not have spaces in between")

elif not username.isalpha():
    print("username can not contain digits")
else:
    print(f"Welcome {username}")