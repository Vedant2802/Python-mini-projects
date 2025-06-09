from abc import ABC, abstractmethod
from typeguard import typechecked

@typechecked
class Car:
    def __init__(self , model , year , color , for_sale):
        self.model= model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"You drive {self.model} car")
    
    def stop(self):
        print("You stop the car")


#class variable = shared among all instances(objects created from that class) of the class
#Defined outside of the constructor method
#Allow to share data among all the objects created from that class

class Student:

    class_year = 2022
    student_num = 0

    def __init__(self,name,age):
        self.name = name
        self.age = age
        if(Student.student_num >= 0):
            Student.student_num += 1

#inheritance
#Allows a class to inherit attributes and methods from another class
#Helps with code reusabilty and extensibility

class Animal:
    def __init__(self , name):
        self.name = name
        self.is_alive = True
    
    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def speak(self):
        print("woof") 
    pass
class Cat(Animal):
    pass
class Mouse(Animal):
    pass


class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass
    @abstractmethod
    def stop(self):
        pass

class Vehicle_My(Vehicle):
    def go(self):
        print("you drive the vehicle")
    def stop(self):
        print("ypu stop the vehicle")

# Super Function 
# Function used in a child class to call methods from a parent class (superclass)
#Allows you to extend the functionaluty of the inherited methods


# class Shape:
#     def __init__(self, color, filled:bool):
#         self.color = color
#         self.filled = filled

#     def name_call(self):
#         print(f"the color is {self.color}")

# class Circle(Shape):
#     def __init__(self, color, filled, radius):
#         super().__init__(color, filled)
#         self.radius = radius
#         # super().name_call()
#     def name_call(self):
#         print(f"the radius is {self.radius}")
#         super().name_call()

# class Square(Shape):
#     def __init__(self, color, filled, width):
#         super().__init__(color, filled)
#         self.width = width

# class Triangle(Shape):
#     def __init__(self, color, filled, width, height):
#         super().__init__(color, filled)
#         self.width = width
#         self.height = height


#Polymorphism (have many forms or faces)

# class Shape:
#     @abstractmethod
#     def area(self):
#         pass

# class Circle(Shape):
#     def __init__(self , radius):
#         self.radius = radius
#     def area(self):
#         return 3.14 * self.radius ** 2

# class Square(Shape):
#     def __init__(self , side):
#         self.side = side
#     def area(self):
#         return self.side ** 2

# class Triangle(Shape):
#     def __init__(self , base , height):
#         self.height=height
#         self.base = base
#     def area(self):
#         return 0.5 * self.base * self.height
# class Pizza(Circle):
#     def __init__(self , name , radius):
#         self.name = name
#         print(f"the pizza name is {self.name}")
#         super().__init__(radius)

# shapes = [Circle(4) , Square(5) , Triangle(6,7) , Pizza("Pizza" , 10)]

# for shape in shapes:
    # print(shape.area())


# duck typing , Another way of polymorphism beside inheritance , object must have the minimum necessary attributes and methods


# class Animal:
#     alive = True

# class Dog(Animal):
#     def speak(self):
#         print("woof")

# class Cat(Animal):
#     def speak(self):
#         print("meow")

# class Cow(Animal):
#     def speak(self):
#         print("Moo")
# # () after the class means that you are creating an object of that class
# animals = [Dog(),Cat(),Cow()]

# for animal in animals:
#     animal.speak()

# Aggregation

# Represents a relationship where one object (the whole) contains reference to one or more INDPENDENT objects (the parts)

# class Library:
#     def __init__(self,name):
#         self.name = name
#         self.books = []
#     def add_book(self,book):
#         self.books.append(book)
    
#     def author_name(self):
#         for name in self.books:
#             print(name.author)
# class Book:
#     def __init__(self , title , author):
#         self.title = title
#         self.author = author

#Library object

# library = Library("NY")

# book1 = Book("Da Vinci Code" , "Dan Brown")
# book2 = Book("Da Vinci" , "Dan Brown")

# library.add_book(book1)
# library.add_book(book2)
# print(library)

# # Composition = The composed object directly owns its components , which cannot exist independently
# #"owns-a" relationship

# class Engine:
#     def __init__(self,horse_power):
#         self.horse_power = horse_power

# class Wheel:
#     def __init__(self,size):
#         self.size = size
# class Car:
#     def __init__(self, make , model , horse_power:int , wheel_size:int):
#         self.make = make
#         self.model = model
#         self.engine = Engine(horse_power)
#         self.wheels = [Wheel(wheel_size) for wheel in range(4)]
#     def display_car(self):
#         return f"{self.make} {self.model}"

# car = Car("ford" , "mustang" , 500 , 18 )

# print(car.display_car())

#Nested Class = A class defined within another class
    #Class Outer:
        #Class Inner:

# Benifits: Allows you to logically group classes that are closely related
# Encapsulates private details that are not relevant outside of the outer class
# Keeps the namespace clean ; reduces the possibiluty of naming conflicts

# class Company:

#     class Employee:
#         # print("This is the first class")
#         def __init__(slef,name,position):
#             self.name = name
#             self.position = position
#         def get_details(self):
#             return f"{self.name} {self.position}"

#     def __init__(self , company_name):
#         self.company_name = company_name
#         self.employees=[]

#     def add_employee(self,name,position):
#         new_employee = self.Employee(name , position)
#         self.employees.append(new_employee)

#     def list_employees(self):
#         pass


# company = Company("Google")
# company.add_employee("Vedant" , "SDE")

# class Nonprofit:

#     class Employee:
#         print("This is the first class")

# Static Method = A method that belong to a class rather thatn any object from that class (instance)
# Static methods = Best for utility functions that do not need access to class data

# class Employee:

#     def __init__(self,name,position):
#         self.name = name
#         self.position = position
    
#     # this is an instance method can be used only on class instances
#     def get_info(self):
#         return f"{self.name} = {self.position}"
    
#     @staticmethod
#     def is_valid_position(position):
#         valid_positions = ["Manager" , "Cashier" , "Cook"]
#         return position in valid_positions

# print(Employee.is_valid_position("cook"))

# Class methods = Allow Operations related to the class itself
    # Take (cls) as the first parameter , which represents the class itself

class Student:

    count = 0
    total_gpa = 0

    def __init__(self,name,gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    #Instance method

    def get_info(self):
        return f"{self.name} {self.gpa}"
    
    
    @classmethod
    def get_count(cls):
        return f"{cls.count}"
    @classmethod
    def get_average(cls):
        if cls.count == 0:
            return 0
        else:
            return f"the average is {cls.total_gpa/cls.count}"


student1 = Student("Akshat" , 4.0)
student2 = Student("Vedant" , 3.0)

print(Student.get_count())

print(Student.get_average())

# Magic Methods (dunder methods) (double underscore methods)
# they are automatically called by many of pythons built in operations
# they allow developers to define and modify the behaviour of objects


class Book:
    def __init__(self,title,author,num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages
    def __str__(self):
        return f"{self.title}:{self.author}"
    def __eq_(self,other):
        return self.title == other.title

book1 = Book("Harry Potter" , "JRR" , 394)
book2 = Book("Harry Potter" , "GMartin" , 410)

print(book1==book2)

#when we pass the arguments inside to create an object inside the Book class the dunder __init__ method is called automatically behind the scenes

print(book1)
