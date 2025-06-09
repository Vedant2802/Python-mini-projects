# Accessing elements of a sequence using[](indexing operator) having three field [start:end:step]

credit_number = "123313-12413-123123-12313"

#prints the first index character
print(credit_number[0])

#start index

print(credit_number[0:]) #this will print everything till the end
print(credit_number[:5]) #this will print chracters starting from 0th inde to 5th index , python assumes the starting index as 0 if the index is not specifed

#step
#suppose you want to print every second character
print(credit_number[::2])

#reverse this string

print(credit_number[::-1])

num = [1,2,3,4,5]
print(num[::-1])

