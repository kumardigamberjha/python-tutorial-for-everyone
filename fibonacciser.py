# a= 0
# b= 1
# 0+1= 1
# 1+1= 2
# 1+2=3
# 2+3=5


a= 0
b= 1
print(a,b, end=" ")
for i in range(10):
    c= a+b
    print(c, end=" ")
    a= b
    b= c