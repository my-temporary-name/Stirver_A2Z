# Count Inversions

# Given an array of integers. Find the Inversion Count in the array.  
# Two array elements arr[i] and arr[j] form an inversion if arr[i] > arr[j] and i < j.

import math
def inversionCount(arr, n):

    def merge(arr, low, mid,  high):
        tmp = []
        left = low
        right = mid+1
        cnt = 0

        while left<=mid and right<=high:

            if arr[left] <= arr[right]:
                tmp.append(arr[left])
                left+=1
            else:
                tmp.append(arr[right])
                cnt += mid-left+1
                right+=1
        
        while left<=mid:
            tmp.append(arr[left])
            left+=1
        while right<=high:
            tmp.append(arr[right])
            right+=1
        
        for i in range(low, high+1):
            arr[i] = tmp[i - low]
        
        return cnt
    
    # --------------------------------------------------------------
    def mergesort(arr, low, high):
        cnt = 0
        if low>=high:
            return cnt
        mid = math.floor((low+high)/2)

        cnt+= mergesort(arr, low, mid)
        cnt+= mergesort(arr, mid+1, high)
        cnt+= merge(arr, low, mid, high)

        return cnt


    return mergesort(arr,0,n-1)





n = 5
arr = [2,4,1,3,5]
print(inversionCount(arr,n))