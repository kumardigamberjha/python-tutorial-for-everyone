# def add(a,b):
#     return a+b

# print(add(5,5))

# def add():
#     print("This is function")

# add()


# types of functions:-

# 1. required argument or positional argument
# 2. keyword argument
# 3. default argument
# 4. variable length


# def add(a,b):
#     print("Add of number is:- ", end="")
#     return a+b

# print(add(4, 6))


# def add(b,a, c):
#     print("Add of number is:- ", end="")
#     print("a", a, "b", b, "c", c)
#     return a+b+c

# print(add(5,6, a= 3))

# def add(b,a=6):
#     print("Add of number is:- ", end="")
#     print("a", a, "b", b)
#     return a+b

# print(add(3, 7))


# *args and **kwargs

# def names(a, b, c):
#     return a,b,c

# print(names('Codin india', 'Dj videos', 'youtube'))




# **kwargs keyword 



# def names(a, *args):
#     return a, args

# # print(names('Codin india', 'dj videos', 'youtube', 'digamber'))



# def names(a,*args, **kwargs):
#     return a,args, kwargs

# print(names('Codin india',*'digamber', 'youtube', **{"1": "codin india", "2": "dj videos"}))














f= open("hlos.txt", 'a')
b= f.write("This is npt a fike")
print(b)