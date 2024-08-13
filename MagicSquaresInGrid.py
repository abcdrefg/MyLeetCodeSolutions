class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:

        def check_if_is_magic(square):
            numbers = set()

            for i in range(3):
                for j in range(3):
                    if square[i][j] > 9 or square[i][j] < 1 or square[i][j] in numbers:
                        return 0
                    numbers.add(square[i][j])

            diagonal_1 = square[0][0] + square[1][1] + square[2][2]
            diagonal_2 = square[0][2] + square[1][1] + square[2][0]
            if diagonal_1 != diagonal_2:
                return 0

            for i in range(3):
                if square[0][i] + square[1][i] + square[2][i] != diagonal_1:
                    return 0
                if square[i][0] + square[i][1] + square[i][2] != diagonal_1:
                    return 0
            return 1

        col_size = len(grid)
        row_size = len(grid[0])

        num_of_squares = 0
        for i in range(col_size - 2):
            for j in range(row_size - 2):
                num_of_squares += check_if_is_magic([
                    [grid[i][j], grid[i][j + 1], grid[i][j + 2]],
                    [grid[i + 1][j], grid[i + 1][j + 1], grid[i + 1][j + 2]],
                    [grid[i + 2][j], grid[i + 2][j + 1], grid[i + 2][j + 2]]
                ])
        return num_of_squares