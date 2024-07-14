# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

from typing import List
def setZeroes(matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])

        row = [0]*n
        col = [0]*m

        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    row[i]=1
                    col[j]=1
        
        for i in range(n):
            for j in range(m):
                if row[i] or col[j]:
                    matrix[i][j]=0
        
        for i in range(n):
             print(matrix[i])


matrix = [[1,1,1],[1,0,1],[1,1,1]]

for i in range(len(matrix)):
    print(matrix[i])
print()
setZeroes(matrix)