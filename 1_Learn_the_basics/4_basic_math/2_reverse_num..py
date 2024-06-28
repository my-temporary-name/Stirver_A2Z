# Given a signed 32-bit integer x, return x with its digits reversed. 
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

n = int(input("Enter a number: "))

if n==0:
    print(0)

if n>0:
    rn = int(str(n)[::-1])

    if rn<= (2**31)-1:
        print(rn)
    else:
        print(0)
else:
    n = n*-1
    rn = int(str(n)[::-1])*-1
    if rn>= (2**31)*-1:
        print(rn)
    else:
        print(0)
