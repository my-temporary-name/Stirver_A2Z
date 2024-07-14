# Missing And Repeating

# Given an unsorted array arr of size n of positive integers. One number 'A' from set {1, 2,....,N} is missing and 
# one number 'B' occurs twice in array. Find these two numbers.

n = 3 
arr=[1,3,3]

from collections import Counter
x = Counter(arr)
twice = None
for i in x:
    if x[i]==2:
        print(f"twice: {i}")
        twice = i
        break

sm = sum(arr) - twice
n_sum = (n*(n+1))//2

print("missing: ", n_sum -  sm)