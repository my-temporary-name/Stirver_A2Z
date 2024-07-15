	
# Largest Subarray with 0 Sum

def maxLen(n ,arr):
    ct = 0
    mpp = {}
    maxi = 0

    for i in range(n):
        ct+=arr[i]
        if ct==0:
            maxi = i+1
        else:
            if ct in mpp:
                maxi = max(maxi, i - mpp[ct])
            else:
                mpp[ct] = i  
    print(maxi)

    return

arr = [15,-2,2,-8,1,7,10,23]
maxLen(len(arr), arr)