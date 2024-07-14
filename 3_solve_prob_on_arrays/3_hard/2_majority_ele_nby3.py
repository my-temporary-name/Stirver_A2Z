# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.


# nums = [3,2,3]
nums = [1,2]

from collections import Counter

x = Counter(nums)
print(x)
n = len(nums)
m = n/3

lst = []

for ele in x:
    if x[ele]>m:
        lst.append(ele)

print(lst)