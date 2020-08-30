# # # parent class

# # # child class


# # # parent class:    isse child class data leta hai isko hum base class v bolte hai
# # # child class:   ye parent class se data drive krta hai  


# # class Person:
# #     def Name(self, name):
# #         self.name= name
# #         print(self.name)

# #     def Age(self, age):
# #         self.age= age
# #         print(self.age)
    
# # p1= Person()
# # p1.name= "Codin India"
# # p1.age= 21
# # print(p1.name, p1.age)


# # # child class

# # class Student(Person):
# #     def Phone(self, phone):
# #         self.phone= phone
# #         print(self.phone)
    
# #     def DOB(self, dob):
# #         self.dob= dob
# #         print(self.dob)

# # s1= Student()

# # s1.name= "DJ Videos"
# # s1.age="20"
# # s1.phone="78145745759"
# # print(s1.name, s1.age, s1.phone)




# class Person:
#     def __init__(self, fname, lname):
#         self.fname= fname
#         self.lname= lname

#     def greetings(self):
#         print("Welcome", self.fname)

# p1= Person("Codin", "India")
# p1.greetings()
# print(p1.fname, p1.lname)


# class Child(Person):
#     def __init__(self, fname, lname,dob):
#         # Person.__init__(self, fname, lname)
#         super().__init__(fname, lname)
#         self.fname= fname
#         self.lname= lname
#         self.dob= dob
    
# c1= Child("Sinni", "Jha","10111999")
# print(c1.fname, c1.lname, c1.dob)
# c1.greetings()



# Types of inheritance

# 1. Single Inheritance

# class parent:
#     def func1(self):
#         print("This is parent class")

# class Child(parent):
#     def func2(self):
#         print("This is Child Class")

# ch1= Child()
# ch1.func1()
# ch1.func2()



# 2. Multiple Inheritance: 

# class Parent:
#     def P1(self):
#         print("This is Parent 1")

# class Parent2:
#     def P2(self):
#         print("This is Parent 2")

# class Child(Parent, Parent2):
#     def Ch1(self):
#         print("This is Child Class")

# object= Child()
# object.P1()
# object.P2()
# # object.Ch1()





# # 3. Multilevel Inheritance


# class A:
#     def func1(self):
#         print("This is A")

# class B(A):
#     def func2(self):
#         print("This is B")

# class C(B):
#     def func3(self):
#         print("This is C")
    
# class D(C):
#     def func4(self):
#         print("This is D")


# obj= D()
# obj.func1()
# obj.func2()
# obj.func3()
# obj.func4()




# Hierarchical Inheritance


# class Parent:
#     def p1(self):
#         print("This is Parent class")

# class Child(Parent):
#     def Ch1(self):
#         print("This is Child 1 Class")

# class Child2(Parent):
#     def Ch2(self):
#         print("This is Child 2")

# ch1= Child()
# ch1.p1()
# ch1.Ch1()


# ch2= Child2()
# ch2.p1()
# ch2.Ch2()



# Hybrid Inheritance



class A:
    def func1(self):
        print('This is Class A')

class B(A):
    def func2(self):
        print("This is class B")

class C(A):
    def func3(self):
        print("this is Class C")

class D(B):
    def func4(self):
        print("This is class D")

class E(C):
    def func5(self):
        print("This is E class")

class F(C):
    def func6(self):
        print("This is Class F")

obj= D()
print("This is Class D object")

obj.func1()
obj.func2()
obj.func4()

print("This is Class E object")
obj1= E()
obj1.func1()
obj1.func3()
obj1.func5()


print("This is Class F object")
obj2= F()
obj2.func1()
obj2.func3()
obj2.func6()

