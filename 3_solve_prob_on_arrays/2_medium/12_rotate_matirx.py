# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).


# Method 1: When you need extra space
from typing import List
def rotate(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    new_mat = []

    for i in range(len(matrix)):
        arr = []
        for j in range(len(matrix)):
            arr.append(matrix[j][i])
        
        new_mat.append(arr[::-1])
    
    matrix[:] = new_mat[:]

    n = len(matrix)
    for i in range(n):
        print(matrix[i])

matrix = [[1,2,3],[4,5,6],[7,8,9]]
n = len(matrix)
for i in range(n):
    print(matrix[i])
print()
rotate(matrix)

# Method 2: Without taking extra space (in - place)
print("-"*50)
from typing import List
def rotate2(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    n = len(matrix)
    for i in range(n):
        for j in range(i):
            matrix[i][j] , matrix[j][i] = matrix[j][i] , matrix[i][j]

    for i in range(n):
        print(matrix[i])
    print()
    # matrix.reverse()

    for i in range(n):
        print(matrix[i][::-1])

matrix = [[1,2,3],[4,5,6],[7,8,9]]
n = len(matrix)
for i in range(n):
    print(matrix[i])
print()
rotate2(matrix)
