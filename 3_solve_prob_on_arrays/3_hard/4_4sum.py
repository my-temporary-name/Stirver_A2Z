# 4 sum
# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target

from typing import List
def fourSum(arr: List[int], x: int) -> List[List[int]]:
    lst = []
    n = len(arr)
    arr.sort()

    for l in range(n):
        if l>0 and arr[l]==arr[l-1]:
            continue

        for i in range(l+1,n):
            if i>l+1 and arr[i]==arr[i-1]:
                continue
            
            j = i+1
            k = n-1

            while j<k:
                sm = arr[i]+arr[j]+arr[k]+arr[l]

                if sm<x:
                    j+=1
                elif sm>x:
                    k-=1
                else:
                    tmp = [arr[i], arr[j], arr[k],arr[l]]
                    lst.append(tmp)
                    j+=1
                    k-=1

                    while j<k and arr[j]==arr[j-1]:
                        j+=1
                    while j<k and arr[k]==arr[k+1]:
                        k-=1
    return lst

nums = [1,0,-1,0,-2,2]
target = 0

print(fourSum(nums, target)) # use same method as 4 sum
