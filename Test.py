# # class
# class MyClass:
#     x = 5


# # object
# p1 = MyClass()

# # print property of that object with that class!
# # print(p1.x)


# class Person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname

#     def printname(self):
#         print(self.firstname, self.lastname)


# p2 = Person("Joe", 19)
# # modify obj
# p2.age = 2
# # delet object propersties
# del p2.age
# # delet object
# del p2

# # print(p2.name)
# # print(p2.age)

# # p2.myfunc()


# # now u won't get any errs :D
# class NonContentialClass:
#     pass


# x = Person("Joe", "Natsa")
# x.printname()


# class Student(Person):
#     def __init__(self, fname, lname, year):
#         # KEEP THE INHERITANCE: Person.__init__(self, fname, lname)
#         super().__init__(fname, lname)
#         self.graduationyear = year

#     def welcome(self):
#         print("Welcome", self.firstname, self.lastname,
#               "to the class of", self.graduationyear)


# y = Student("MADAR", "FAKAR", 1992)
# y.welcome()

# from ast import literal_eval
# userInput = input(' ENTER SOMETHING: ')

# if userInput == type(str):
#     print("IT'SSSS")


# def get_type(input_data):
#     try:
#         return type(literal_eval(input_data))
#     except (ValueError, SyntaxError):
#         # A string, so return str
#         return str


# print(get_type("1"))        # <class 'int'>
# print(get_type("1.2354"))   # <class 'float'>
# print(get_type("True"))     # <class 'bool'>
# print(get_type("abcd"))     # <class 'str'>

# b = isinstance(1, int)

# print(not b)
