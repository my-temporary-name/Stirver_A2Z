# maximum-product-subarray

def maxProductSubArray(arr):
    mx = arr[0]
    mn = arr[0]
    result = mx

    for i in range(1, len(arr)):
        curr = arr[i]
        temp = max(curr, mx*curr, mn*curr)
        mn = min(curr, mx*curr, mn*curr)

        mx = temp

        result = max(result , mx)
    return result


if __name__ == "__main__":
    nums = [1, 2, -3, 0, -4, -5]
    print("The maximum product subarray:", maxProductSubArray(nums))