# Find Missing Number in array
nums = [9,6,4,2,3,5,7,0,1]
n = len(nums)

summ = (n*(n+1))//2

print("Missing: ", summ - sum(nums))