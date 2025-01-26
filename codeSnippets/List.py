#main methods

# my_num = [1,4,5]

# if (6 not in my_num):
#     print("Akshat Vedant")

from typing import List

nums=[1,2,3,3,3,3,3,4,5,5]

# def count_x(nums: List[int] , x:int):
#     length = len(nums)
#     result=0
#     for i in range(length):
#         if(x==nums[i]):
#             result = result+1
#     print(result)
# count_x(nums,3)

#Built in functions for lsit of integers

# print(sum(nums))

# print(max(nums))
# print(min(nums))

def get_sum(n:List[int])->int:
    sum=0
    for i in range(len(n)):
        sum = sum + n[i]
    return sum

value = get_sum(nums)
print(value)

def get_max(n:List[int])->int:
    max_value=0
    for i in range(len(n)):
        if(n[i]>max_value):
            max_value=n[i]
    return max_value

value1 = get_max(nums)
print(value1)