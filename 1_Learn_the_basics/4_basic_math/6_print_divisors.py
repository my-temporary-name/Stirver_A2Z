# Given a positive integer N., The task is to find the value of Σi from 1 to N F(i) where function F(i) for the number i is defined as the sum of all divisors of i.

n = int(input("Enter a number: "))

ct = 0

for i in range(1,n+1):
    k = n//i # k is the number of times i divides n
    ct += i*k

print(ct)

# Input:
# N = 4
# Output:
# 15
# Explanation:
# F(1) = 1
# F(2) = 1 + 2 = 3
# F(3) = 1 + 3 = 4
# F(4) = 1 + 2 + 4 = 7
# ans = F(1) + F(2) + F(3) + F(4)
#     = 1 + 3 + 4 + 7
#     = 15

# Working of our code:
# 1 divides 4 4 times, 2 divides 4 2 times, 3 divides 4 1 time, 4 divides 4 1 time
# 1*4 + 2*2 + 3*1 + 4*1 = 4 + 4 + 3 + 4 = 15
