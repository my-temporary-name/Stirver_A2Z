# Problem Statement: Given an array consisting of only 0s, 1s, and 2s. 
# Write a program to in-place sort the array without using inbuilt sort functions. ( Expected: Single pass-O(N) and constant space)

def do_something(nums):
    ## Method 1

    # low = 0
    # mid = 0
    # high = len(arr)-1

    # while mid<=high:
    #     if arr[mid] == 0:
    #         arr[mid], arr[low] == arr[low], arr[mid]
    #         mid+=1
    #         low+=1
    #     elif arr[mid]==1:
    #         mid+=1
    #     else:
    #         arr[mid],arr[high] == arr[high],arr[mid]
    #         high-=1
    #     print(arr)
    # print(arr)


    ## Method 2 -----------------------------------------------------
    zero=0
    one=0
    two=0

    for i in range(len(nums)):
        if nums[i]==0:
            zero+=1
        elif nums[i]==1:
            one+=1
        else:
            two+=1
    
    nums[:] = [0]*zero + [1]*one + [2]*two
    print(nums)
    
    


arr = [2,0,2,1,1,0]
do_something(arr)
# print(arr , x)