try:
    a= int(input("Enter a number: "))
except:
    print("Number expected")
b= 4
try:
    print(a/b)
except:
    print("Number can't be divided by 0")