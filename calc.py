'''
1. user se input
2. options - add, subs, divide, multiply
3. user input
4. operations inputs pe
'''

print("Select the operation you want to perform: ")
userinput= int(input("1.Add\n2.substact\n3.multiply\n4.Divide\n5.Exit\n"))

if userinput==5:
    print("bubyee")
    exit()

input1= int(input("Enter 1st Number: "))
input2= int(input("Enter 2nd Number: "))
if userinput==1:
    print("Add: ",input1+input2)

elif userinput==2:
    print("Substract: ", input1-input2)

elif userinput==3:
    print("Multiply: ", input1* input2)

elif userinput==4:
    print("Divide: ", input1/input2)

else:
    print("Invalid input")