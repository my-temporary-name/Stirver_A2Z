# Merge intervals

# Given an array of intervals where intervals[i] = [start_i, end_i], merge all overlapping intervals, 
# and return an array of the non-overlapping intervals that cover all the intervals in the input.

def merge(arr):
    arr.sort()
    res = 0
    for i in range(1, len(arr)):
        if arr[res][1] >= arr[i][0]:
            arr[res][i] = max( arr[res][1], arr[i][1])
        else:
            res+=1
            arr[res] = arr[i]

    lst =[]
    for i in range(res+1):
        lst.append(arr[i])
    
    print(lst)


    return

intervals = [[1,3],[2,6],[8,10],[15,18]]
merge(intervals)