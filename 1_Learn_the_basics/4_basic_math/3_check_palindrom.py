# Given an integer x, return true if x is a palindrome , and false otherwise.

x = int(input("Enter a number: "))

if x<0:
    print(False)

else:
    print(x == int(str(x)[::-1]))
