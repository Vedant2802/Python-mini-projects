# str_name = "Akshat Vedant"

# print(str_name[1:4])

# if you do not specify the starting and the ending index so in that case
# if starting is not specified it will assume that the starting is from 0.
# if the ending is not specified it will assume that the endling is at the last index

# def last_n_caharacters(word:str , n:int):
#     # index = len(word)-n
#     # return(word[index:])
#     return(word[-n:])

# value = last_n_caharacters("Akshat Vedant" , 5)
# print(value)

# Reversing a string

def say_goodbye(name:str , age:int):
    print(f"Say Goodbye {name} , you are {age} years old")

say_goodbye("Akshat" , 28)