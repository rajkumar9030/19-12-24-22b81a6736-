from sympy import *
def prime(num):
    if isprime(num):
        return True
    else:
        return False
        
num = int(input("Enter a number: "))
if(prime(num)):
    print("Prime")
else:
    print("Not Prime")