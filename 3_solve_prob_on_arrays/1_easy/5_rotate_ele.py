# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
# eg: 
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]


nums = [1,2,3,4,5,6,7]
k = 3
print(nums)
k = k % len(nums)
for i in range(k):
    x = nums.pop()
    nums.insert(0,x)

print(nums)