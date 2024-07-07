# Check if Array is Sorted and Rotated


def check(nums):
    x = nums+nums
    nums.sort()
    print(x, nums)

    for i in range(len(x)-len(nums)):
        if x[i:len(nums)+i] == nums[:]:
            return True
    
    return False

print(check([3,4,5,1,2]))

print("---------------------------")
# In TC = O(N)

def solve(arr):
    j = 0
    while(j< len(arr)-1  and  arr[j]<=arr[j+1]):
        j+=1
    
    res = arr[j+1: ] + arr[:j+1]
    print(res)
    
    for i in range(len(res)-1):
        if res[i]>res[i+1]:
            print(res[i], res[i+1] , i, i+1)
            return False
    
    return True

print(solve([3,4,5,1,2]))