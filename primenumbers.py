x =int(input("Enter a number:"))
F:int=0
if (x==1):
    print(x," is a not a prime number")

elif (x==2):
    print(x," is a prime number")


elif(x>=3):
    for i in range(2, (x-1)):
        if (x%i)==0:
            F=1

if(F==1):
    print(x," is a not a prime number")
else:
    print(x, " is a prime number")


