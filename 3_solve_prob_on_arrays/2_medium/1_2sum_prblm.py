# 2 sum problem
# for sorted array
def sort_two_sum(arr, target):
    left = 0
    right = len(arr)-1

    while left<=right:
        sm = arr[left] + arr[right]
        if sm==target:
            print(arr[left] , arr[right])
            return
        elif sm<target:
            left+=1
        else:
            right-=1
    print("-1,-1")


arr = [2,6,5,8,11]
target = 14
sort_two_sum(arr, target)

# for unsorted arr ----------------------------------------------------------------------


arr = [2,7,11,15,4]
target = 9

x,y = None, None

for i in range(len(arr)):
    x = arr[i]
    sm = target - x
    if sm in arr and arr.index(sm)!=i:
        print(x , sm)
        break

