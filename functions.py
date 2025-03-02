import math

# write a function to return a square of a number

# n = int(input("Enter the number : "))

# def square(n):
#     return n**2

# value = square(2)
# print(value)

# 2 . function that take two params and return their sum

# def two_sum(a: int, b: int) -> int:
#     if not (isinstance(a, int) and isinstance(b, int)):
#         raise TypeError("Both arguments must be integers")
#     return a + b

# value = two_sum("Akshat","Vedant")
# print(value)

# 3. Multiple returns

# def circle(radius:int)->int:
#     area = math.pi*(radius**2)
#     circumference = 2*math.pi*radius
#     new_list = []
#     new_dict = {}
#     # new_list.append(area)
#     # new_list.append(circumference)
#     new_dict["area"] = math.floor(area)
#     new_dict["circumference"] = math.floor(circumference)
#     # return new_list
#     return new_dict

# value = circle(4)
# print(value.get("area"))
# print(value)

# lambda function
# print the cube of a number

# cube = lambda x:x**3
# print(cube(3))

# functions with *args

# def sum_all(*args):
#     print(args)
#     for i in args:
#         print(i*2)
#     return sum(args)

# value = sum_all(1,2,3,4,5)
# print(value)

#  functions with **kwargs

# def print_names(**kwargs):
#     print(kwargs)
#     for key,values in kwargs.items():
#         print(f"the key is {key} , the Value is {values}")

# print_names(name="Akshat")

# generator function that yields even number upto a limit

# recursive function for factorial

# def recursive_call(num:int)->int:
#    if num==0:
#     return 1
#    else:
#     return num* recursive_call(num-1)

# value = recursive_call(5)
# print(value)

# my_num = [10,256,378,4,5,6,]
# filtered_num = list(reversed(my_num))
# print(filtered_num)