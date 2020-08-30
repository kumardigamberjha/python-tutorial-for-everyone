# # Functions ki help se Polymorphism 

# class Fruit:
#     def name(self):
#         print("This is Mango")

#     def color(self):
#         print("Yellow")

# class Vegitable:
#     def name(self):
#         print("This is Tomato")

#     def color(self):
#         print("red")

# def common(obj):
#     obj.name()
#     obj.color()

# f1= Fruit()
# v1= Vegitable()

# common(f1)
# common(v1)




# class polymorphism

# class India:
#     def capital(self):
#         print("New Delhi")

#     def language(self):
#         print("Hindi")

# class USA:
#     def capital(self):
#         print("Washigton DC")

#     def language(self):
#         print("English")

# # Object creation
# indian= India()
# american= USA()

# # indian.capital()
# # indian.language()

# # american.capital()
# # american.language()


# # for loop ki help se use kr sktte hai

# for country in (indian, american):
#     country.language()
#     country.capital()




#  polymorphism using inheritance

class Marriage:
    def intro(self):
        print("There are 2 type Marriage")

    def type(self):
        print("Tell Me The Type of Your marriage")

class LoveMarraige(Marriage):
    def type(self):
        print("Love Marriage")

class ArrangeMarriage(Marriage):
    def type(self):
        print("Arrange marriage")

arrange= ArrangeMarriage()
love= LoveMarraige()

arrange.intro()
arrange.type()

love.intro()
love.type()