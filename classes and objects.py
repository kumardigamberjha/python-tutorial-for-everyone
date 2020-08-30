# syntax of classes

# class class_name:
#     """
#     apne codes
#     """


# class myfirstclass:
#     name= "digamber"


# my= myfirstclass()
# print(my.name)


# class student:
#     name="Codin India"

# s1= student()
# print(s1.name)


# init()

# class student:
#     def __init__(self, name, age):
#         self.name= name
#         self.age= age

# s1= student("Digamber", 20)
# print(s1.name, s1.age)


# Objects methods / behaviour


class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        print("Hello! "+ self.name)

s1 = student("Digamber", 20)
print(s1.name, s1.age)

s2= student("Sinni", 21)
print(s2.name, s2.age)

s1.greeting()
s2.greeting()

# s1.name= "Codin India"
# print(s1.name)


#modify object properties

s1.name= "Shubham"
print(s1.name)


# delete the properties of the object

# del s1.age
# print(s1.age)

# delete the object

del s1


print(s1.name)
print(s2.name)