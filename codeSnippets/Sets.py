from typing import List
# my_set = set()

# my_set.add(4)
# my_set.add(5)
# my_set.add(4)

# print(my_set)

#given a list of numbet create a set of those numbers
nums=[1,2,3,4,5,5,6,7,7]
def set_number(n: List[int] )->set[int]:
    result_set = set()
    for i in range(len(n)):
        result_set.add(n[i])
    return result_set

value = set_number(nums)
print(value)