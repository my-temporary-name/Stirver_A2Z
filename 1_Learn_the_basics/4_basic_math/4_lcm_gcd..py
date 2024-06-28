# Given two integers a and b, write a function lcmAndGcd() to compute their LCM and GCD. 
# The function takes two integers a and b as input and returns a list containing their LCM and GCD.


def gcd(a,b):
    if b==0:
        return a
    return gcd(b, a%b)




a = 5
b = 10
print(gcd(a,b), a*b//gcd(a,b))

a = 14
b = 8
print(gcd(a,b), a*b//gcd(a,b))