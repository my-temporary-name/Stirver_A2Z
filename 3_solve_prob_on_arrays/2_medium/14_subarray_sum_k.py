# Sub array Sum Equals K

# Given an array of integers nums and an integer k, return the total number of sub arrays whose sum equals to k.
# A sub array is a contiguous non-empty sequence of elements within an array.

# Example 1:
# Input: nums = [1,1,1], k = 2
# Output: 2

# Example 2:
# Input: nums = [1,2,3], k = 3
# Output: 2


# Iterate through the array:

# 1. For each element in the array, add it to preSum.
# 2. Calculate remove as preSum - k. This value helps to determine if there is a prefix sum that, when removed, leaves a sum of k.
# 3. If remove is in mpp, it means there are sub-arrays that sum to k. Increment cnt by the count of remove in mpp.
# 4. Update mpp with the current preSum.

from collections import defaultdict
def findAllSubarraysWithGivenSum(arr, k):
    n = len(arr)
    mpp = defaultdict(int)
    preSum  = 0
    cnt = 0

    mpp[0] = 1 # setting 0 in the map

    for i in range(n):
        preSum+=arr[i] # add current element to prefix sum

        # calculate x - k
        remove = preSum - k # This value helps to determine if there is a prefix sum that, when removed, leaves a sum of k.

        # add the number of subarrays to be removed
        cnt += mpp[remove]

        # update the count of prefix sum in map
        mpp[preSum]+=1

        print(mpp , cnt)


    return cnt


if __name__ == '__main__':
    arr = [3, 1, 2, 4]
    k = 6
    cnt = findAllSubarraysWithGivenSum(arr, k)
    print("The number of subarrays is:", cnt)


# easy code:
def findAllSubarraysWithGivenSum(nums, k):
    sum_count={0:1}
    count=0
    current_sum=0

    for i in nums:
        current_sum+=i

        if current_sum-k in sum_count:
            count+=sum_count[current_sum-k]
        if current_sum in sum_count:
            sum_count[current_sum]+=1
        else:
            sum_count[current_sum]=1
    return count

if __name__ == '__main__':
    arr = [3, 1, 2, 4]
    k = 6
    cnt = findAllSubarraysWithGivenSum(arr, k)
    print("The number of subarrays is:", cnt)
