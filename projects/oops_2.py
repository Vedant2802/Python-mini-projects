from car import Car
from car import Student
from car import Dog , Cat , Mouse , Vehicle , Circle , Square , Triangle , Library , Book
from abc import ABC , abstractmethod

# class Car:
#     def __init__(self , model , year , color , for_sale):
#         self.model= model
#         self.year = year
#         self.color = color
#         self.for_sale = for_sale


# car1 = Car("BMW" , 2022 , "Black" , False)
# print(car1.for_sale)

# print(car1)
#the prints the memory address of the object
# <__main__.Car object at 0x1006effd0>
#TO access the atrribute you use the dot , it is called the attribue access operator
# print(car1.model)

# car1.drive()
# print(car1.drive())

# Class variables

# student1 = Student("Akshat" , 25)
# student2 = Student("VEdant" , 26)

# print(student1.class_year)
# print(student2.class_year)

# print(Student.student_num)


#Inheritance

# dog1 = Dog("Scooby")
# you can assign attributes to the objects on the fly if required
# dog1.age = 10
# print(dog1.name)
# print(dog1.age)
# print(dog1.is_alive)
# dog1.sleep()
# dog1.speak()

#Multiple Inheritance (Children inheriting from more than one parent class)

#Abstract class: A class that cannot be instantiated on its own;
#meant to be subclassed , They can contain methods,which are declared but have not implementation.
#requires children to use inherited abstract methods

# vehicle = Vehicle()

#when you run this you get this error
#TypeError: Can't instantiate abstract class Vehicle with abstract methods go, stop

#Super Class

# circle1 = Circle("red",True,5)

# print(circle1.radius)
# circle1.name_call()

# Aggregation

library = Library("NY")

book1 = Book("Da Vinci Code" , "Dan Brown")
book2 = Book("Da Vinci" , "Dan Brown")

library.add_book(book1)
library.add_book(book2)

print(library.author_name())

