# Given an integer array nums, find the sub-array  with the largest sum, and return its sum.

# Kadane's Algorithm, maximum subarray sum

arr = [-2,1,-3,4,-1,2,1,-5,4]

mx = -99999
sm = 0

for i in range(len(arr)):
    sm+=arr[i]

    if sm<arr[i]:
        sm = arr[i]
        
    mx = max(sm , mx)

print(mx)

# Print subarray with maximum subarray sum (extended version of above problem)

arr = [-2,1,-3,4,-1,2,1,-5,4]

mx = -99999
sm = 0

start = 0
ansStart , ansEnd = -1, -1

for i in range(len(arr)):

    if sm==0:
        start = i
    sm+=arr[i]

    if sm>mx:
        mx = max(mx , sm)
        ansStart = start
        ansEnd = i

    if sm<0:
        sm = 0

print(mx , ansStart, ansEnd)