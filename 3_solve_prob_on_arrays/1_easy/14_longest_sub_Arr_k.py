# Longest Sub-Array with Sum K

# Given an array arr containing n integers and an integer k. 
# Your task is to find the length of the longest Sub-Array with the sum of the elements equal to the given value k.

arr = [10, 5, 2, 7, 1, 9]
k = 15

n = len(arr)

preSumMap = {}
sm = 0
mx = 0

for i in range(n):
    sm+=arr[i]
    print(f"i: {i}, sum: {sm}")
    if sm==k:
        mx = max(mx, i+1)
    rem = sm - k
    print(f"rem: {rem}")
    if rem in preSumMap:
        length = i - preSumMap[rem]
        mx = max(mx, length)
        print("ms: ",mx)
    
    if sm not in preSumMap:
        preSumMap[sm] = i
    print(preSumMap)
    print()
print(mx)