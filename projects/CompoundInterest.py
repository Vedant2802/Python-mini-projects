# compound intereset calculator

principle = 0
rate = 0 
time = 0

# while principle <= 0:
#     principle = float(input("Enter the principle amount"))

#     if principle <=0:
#         print("principle can not be less than 0")

# while rate <= 0:
#     rate = float(input("Enter the rate percent"))

#     if rate <=0:
#         print("rate can not be less than 0")

# while time <= 0:
#     time = float(input("Enter the time amount"))

#     if time <=0:
#         print("time can not be less than 0")

# total = principle * pow((1 + rate/100),time)

#If you wan to include 0 values you can write like this

while True:
    principle = float(input("Enter the principle amount"))

    if principle <0:
        print("principle can not be less than 0")
    else:
        break

while True:
    rate = float(input("Enter the rate percent"))

    if rate <0:
        print("rate can not be less than 0")
    else:
        break

while True:
    time = float(input("Enter the time amount"))

    if time <0:
        print("time can not be less than 0")
    else:
        break

total = principle * pow((1 + rate/100),time)
print(f"the total amount is {total}")