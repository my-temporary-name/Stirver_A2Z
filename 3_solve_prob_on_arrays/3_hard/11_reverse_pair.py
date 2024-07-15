
# Given an integer array nums, return the number of reverse pairs in the array.

# A reverse pair is a pair (i, j) where:

# 0 <= i < j < nums.length and
# nums[i] > 2 * nums[j].
 

# Example 1:

# Input: nums = [1,3,2,3,1]
# Output: 2
# Explanation: The reverse pairs are:
# (1, 4) --> nums[1] = 3, nums[4] = 1, 3 > 2 * 1
# (3, 4) --> nums[3] = 3, nums[4] = 1, 3 > 2 * 1

from typing import List
def reversePairs(nums: List[int]) -> int:

    # def merge(arr, low, mid, high):
    #     temp = []  # temporary array
    #     left = low  # starting index of left half of arr
    #     right = mid + 1  # starting index of right half of arr

    #     # storing elements in the temporary array in a sorted manner
    #     while left <= mid and right <= high:
    #         if arr[left] <= arr[right]:
    #             temp.append(arr[left])
    #             left += 1
    #         else:
    #             temp.append(arr[right])
    #             right += 1

    #     # if elements on the left half are still left
    #     while left <= mid:
    #         temp.append(arr[left])
    #         left += 1

    #     # if elements on the right half are still left
    #     while right <= high:
    #         temp.append(arr[right])
    #         right += 1
        
    #     for i in range(low, high+1):
    #         arr[i] = temp[i-low]


    
    # def countPairs(arr, low, mid, high):
    #     right = mid+1
    #     ct = 0

    #     for i in range(low,mid+1):
    #         while right<=high and arr[i]>2*arr[right]:
    #             right+=1
    #         ct+= (right-(mid+1))
    #     return ct

    # def mergeSort(arr, low, high):
    #     cnt = 0
    #     if low >= high:
    #         return cnt
    #     mid = (low + high) // 2
    #     cnt += mergeSort(arr, low, mid)  # left half
    #     cnt += mergeSort(arr, mid + 1, high)  # right half
    #     cnt += countPairs(arr, low, mid, high)  # Modification
    #     merge(arr, low, mid, high)  # merging sorted halves
    #     return cnt
    
    # return mergeSort(nums, 0, len(nums)-1)

    def merge_sort(start,end):
        if(start>=end):
            return 0
        mid=(start+end)//2
        count=merge_sort(start,mid)+merge_sort(mid+1,end)
        i=start
        j=mid+1
        while(i<=mid and j<=end):
            if(nums[i]>2*nums[j]):
                count+=mid-i+1
                j+=1
            else:
                i+=1
        nums[start:end+1]=sorted(nums[start:end+1])
        return count

    return merge_sort(0,len(nums)-1)

nums = [1,3,2,3,1]
print(reversePairs(nums))