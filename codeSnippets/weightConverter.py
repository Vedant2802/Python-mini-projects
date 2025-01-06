
weight = float(input("Enter the weight: "))
unit = input("Enter the unit: ")

if unit == "kg":
    weight = weight * 2.20462
    print(f"The weight in pounds is {weight}")
elif unit == "lb":
    weight = weight / 2.20462
    print(f"The weight in kilograms is {round(weight,2)}")
else:
    print(f"Invalid unit: {unit}")