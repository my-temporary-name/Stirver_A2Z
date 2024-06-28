# Given a number N. Count the number of digits in N which evenly divide N.
# Note :- Evenly divides means whether N is divisible by a digit i.e. leaves a remainder 0 when divided.

n = int(input("Enter: "))

ns = n
ct = 0
while ns:
    last = ns%10
    ns = ns//10
    if last!=0 and n%last==0:
        ct+=1
print(ct)

