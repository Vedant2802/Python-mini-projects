# Tuples are immutable unlike Lists , they are very much similar to Lists

my_sum = (12,35,5)

print(sum(my_sum))

# we can not call append or pop inside a tuple because they will modify the value of the tuple , and by definition
# that is not possible , because tuples are immutable