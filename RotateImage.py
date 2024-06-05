class Solution:
    def rotate(self, matrix) -> None:
        col_size = len(matrix)
        row_size = len(matrix[0])
        for i in range(col_size):
            for j in range(row_size):
                element_to_replace = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = element_to_replace
        """
        Do not return anything, modify matrix in-place instead.
        """

Solution().rotate([[1,2,3],[4,5,6],[7,8,9]])