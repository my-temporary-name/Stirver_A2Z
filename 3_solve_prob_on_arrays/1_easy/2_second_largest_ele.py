# second largest element in arr
# First largest:
# 1. We can get by arr.sort() and return arr[-1] , TC = O(nlogn)
# 2. We can get by max(arr), TC = O(n)
# 3. or by iterating over arr and keep track of max element, TC = O(n)


# To get Second largest element:

# 1. Brute force:
# return arr.sort()[-2] or return sorted(arr)[-2] , TC = O(nlogn)

# 2. Efficient: Single Pass solution
# TC = O(N), SC = O(1)


def secondLargest(arr):

    if len(arr)<2:
        return -1
    
    large = float("-inf")
    s_large = float("-inf")

    for i in range(len(arr)):
        if arr[i]>large:
            s_large = large
            large = arr[i]

        elif arr[i]>s_large and arr[i]!=large:
            s_large = arr[i]
    
    return s_large

print(secondLargest([1, 2, 4, 7, 7, 5]))