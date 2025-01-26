# message = "My name is Akshat"

# print(message)

# message = "My name is Forntend"

# print(message)

# msg1 , msg2 = "hello" , "world"
# msg1 , msg2 = msg2 , msg1

# print(msg1)
# print(msg2)

# print(type(False))

# def greet():
#     print("hello world")
# # invoking the function
# greet()

# def farewell(name):
#     text = "Goodbye , " + name
#     print(text)

# farewell("Akshat")

# def two_sum(num1 , num2):
#     print(num1+num2)

# two_sum(2,3)

# def three_sum(num1 , num2 , num3):
#     print(num1+num2+num3)

# three_sum(1,2,3)

# def product(num1,num2):
#     return (num1*num2)

# result = product(2,3)
# print(result)

# def is_truthy(value):
#     if value:
#         return"Truthy"
#     return "Falsy"

# print(10 , "is a" , is_truthy(0))

# i = 0

# while i<100:
#     print(i)
#     i+=10

# for i in range(3,10):
#     print(i)

# for i in range(10,100,10):
#     print(i)

# for i in range(20,9,-2):
#     print(i)

# for i in reversed(range(10,21)):
#     print(i) 

# for i in range(3,6):
#     for j in range(3,6):
#         print(i,j)


# for i in range(1,6):
#     for j in range(1,6):
#         print(j*"*")
#     break


# for i in range(1,6):
#     print(i*"*")


  # This determines the height of the pattern (can be adjusted)

# def start(n):
#     for i in range(1, n+1, 2):  
#         spaces = (n - i) // 2 
#         print(" " * spaces + "*" * i) 

    
# start(10)

# my_str = "hello"

# print(my_str[0])

# def str_length(word:str):
#     print(word[0])

# str_length("Akshat")

# my_string = "Akshat Vedant"

# # for i in range(len(my_string)):
# #     print(my_string[i])

# for c in my_string:
#     print(c)


def print_char(word1:str , word2:str):
    for char1 in word1:
        print(char1)
    for char2 in word2:
        print(char2)

print_char("Akshat" , "Vedant")
