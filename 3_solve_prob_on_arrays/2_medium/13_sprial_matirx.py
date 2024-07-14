# Given an m x n matrix, return all elements of the matrix in spiral order.

from typing import List
def spiralOrder(arr: List[List[int]]) -> List[int]:
    r = len(matrix)
    c = len(matrix[0])

    top = 0
    left = 0

    right = c-1
    bottom = r-1

    lst = []

    # -----------------------------------------------

    while top<=bottom and left<=right:

        # for top row
        for i in range(left,right+1):
            lst.append(arr[top][i])
        top+=1

        # for right column
        for i in range(top,bottom+1):
            lst.append(arr[i][right])
        right-=1

        # for bottom row
        if top<=bottom:
            for i in range(right, left-1, -1):
                lst.append(arr[bottom][i])
            bottom-=1
        
        # for left column
        if left<=right:
            for i in range(bottom, top-1, -1):
                lst.append(arr[i][left])
            left+=1
    print(lst)

    return


matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
spiralOrder(matrix)


