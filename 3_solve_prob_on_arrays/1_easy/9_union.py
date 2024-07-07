# Union of arrays

arr1 = [1,2,3,4,5]
arr2 = [1,2,3,6,7]

un_set = set()

for i in range(len(arr1)):
    un_set.add(arr1[i])

for i in range(len(arr2)):
    un_set.add(arr2[i])

print(sorted(list(un_set)))