#Very much similar to Objects in JS

# represented by an Empty {} braces

#example given a list return a dictionary

from typing import List , Dict

my_strings = ["akshat" , "vedant" , "name"]

def list_to_dict(n: List[str])-> Dict[str, int]:
    my_dict = {}
    for i in range(len(n)):
        my_dict[i] = n[i]
    return my_dict

value = list_to_dict(my_strings)

print(value)