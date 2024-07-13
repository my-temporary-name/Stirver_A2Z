# find majority element in arr

nums = [2,2,1,1,1,2,2]

ct = 0
ele = None
for i in range(len(nums)):
    if ct==0:
        ct+=1
        ele=nums[i]
    elif nums[i]==ele:
        ct+=1
    else:
        ct-=1

ct2 = 0
for i in range(len(nums)):
    if nums[i]==ele:
        ct2+=1

if ct2>(len(nums)/2):
    print(ele)
else:
    print("-1")