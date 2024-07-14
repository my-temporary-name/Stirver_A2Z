# 3 sum problem

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0


# Method 1: Brute force using 3 loops
from typing import List
def threeSum(arr: List[int]) -> List[List[int]]:
    lst = []
    n = len(arr)
    st = set()

    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if arr[i]+arr[j]+arr[k]==0:
                    lst2 = [arr[i], arr[j], arr[k]]
                    lst2.sort()
                    st.add(tuple(lst2))
                
    
    return [list(item) for item in st]

nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))

# Method 2: Optimized solution

from typing import List
def threeSum2(arr: List[int]) -> List[List[int]]:
    n = len(arr)
    lst = []
    arr.sort()

    for i in range(n):
        if i!=0 and arr[i]==arr[i-1]:
            continue

        j = i+1
        k = n-1

        while j<k:
            sm = sum([arr[i], arr[j], arr[k]])

            if sm<0:
                j+=1
            elif sm>0:
                k-=1
            else:
                tmp = [arr[i], arr[j], arr[k]]
                lst.append(tmp)
                j+=1
                k-=1

                while j<k and arr[j]==arr[j-1]:
                    j+=1
                
                while j<k and arr[k]==arr[k+1]:
                    k-=1
    
    return lst




nums = [-1,0,1,2,-1,-4]
print(threeSum2(nums))

