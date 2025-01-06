import math

a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = math.sqrt(pow(a,2) + pow(b,2))
print(f"The length of the hypotenuse is {round(c,5)}")