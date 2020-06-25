# global variables
 

# print(a)
# print("This is a: ")
a= 10 
a= 15

def add(a, b):
    a= 20
    print("Local variable a: ",a)

    return a+b
print("Global variable a: ", a)

print(add(a, 6))