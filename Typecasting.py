name = "Akshat Vedant"
age = 24
gpa = 3.35
is_student = True

#get the type of the variable
# this does not print anything
type(name)
type(age)
type(gpa)
type(is_student)
#To print the type we write like this
print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

#typecast gpa to integer
gpa = int(gpa)
print(type(gpa))

# typecast age to float
age = float(age)
print(type(age))

# age to string
age = str(age)
print(type(age))

# name to boolean
name = bool(name)
print(type(name))# this actually gives true even if change the string of name
# but if you make the string empty it will give a False