# A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

# For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].

# Python program to print all permutations 

lst = []
def permute(a , l , r):
    if l==r:
        print(a)
        lst.append(a.copy())
    else:

        for i in range(l,r+1):
            a[l], a[i] = a[i] , a[l]
            permute(a , l+1 , r)
            a[l], a[i] = a[i], a[l]



string = "ABC"
n = len(string) 
a = list(string) 
permute(a, 0, n-1) 

print(f"list is : {lst}")

# ------------------------------------------------------------------------------------
