# program 1

import time

# number = [-1,-2,3,-45, -6, 5,-7,8]
# count = 0
# for i in number:
#     if(i>0):
#         count+=1
# print(count)

# Calculate the sum of even numbers upto a  number n

# givenNumber = int(input("Enter the number: "))
# sum = 0

# for i in range(givenNumber+1):
#     if i%2==0:
#         sum+=i
# print(sum)

# problem 3

# Reverse string using loop

# name ="Akshat"

# reversedString=""

# for char in name:
#     reversedString = char+reversedString
# print(reversedString)

# problem 4
# find the first non repeated character

# string = "Aakkssshhatassh"
# char_count={}

# count = 0

# for char in string:
#     if string.count(char) == 1:
#         print(char)
# using dictionary
# for char in string:
#     if char in char_count:
#         char_count[char]+=1
#     else:
#         char_count[char]=1 

# for char in string:
#     if char_count[char]==1:
#         print(char)
# print(char_count)

# Problem 5
# factorial using while loop

# number = 5
# factorial = 1

# while(number>0):
#     factorial = factorial*number
#     number = number - 1

# print(factorial)

# problem = 6
# if duplicate then break out of loop and print the vlaue

arr = ["Akshat", "Aksaht", "Akshat", "Vedant", "Vrrrrr" , "Vedant"]
 
frequency = set()

for item in (arr):
    if item in frequency:
        print(item)
        continue
    frequency.add(item)

# problem 6 exponential backoff strategy , doubles the time after retries but stops after 5 retries

wait_time = 1
max_retries = 5
attempts = 0

while attempts < max_retries:
    print("attempts" , attempts)

    time.sleep(wait_time)
    wait_time *= 2
    attempts += 1

    if attempts == 5:
        break

