class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        column_size = len(matrix)
        row_size = len(matrix[0])

        mid = (column_size - 1) // 2
        low = 0
        high = mid
        if target >= matrix[mid][0]:
            if target == matrix[mid][0]:
                return True
            low = mid
            high = column_size - 1

        while low < high:
            mid = low + (high - low) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                low = mid + 1
            else:
                high = mid - 1

        if target >= matrix[low][0]:
            mid = low

        if target >= matrix[high][0]:
            mid = high

        while True:
            try:
                if target < matrix[mid][0]:
                    mid -= 1
                    continue
                break
            except:
                return False

        array_to_search = matrix[mid]
        low = 0
        high = row_size - 1

        while low <= high:
            mid = low + (high - low) // 2
            if array_to_search[mid] == target:
                return True
            elif array_to_search[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return False

Solution().searchMatrix([[-8,-6,-6,-4,-2,-1,-1,-1,0,1,2,4,6,7,7],[10,10,12,13,13,14,14,16,17,17,17,17,17,18,19],[22,24,26,28,29,31,32,34,34,34,34,36,38,39,39],[40,40,41,43,43,44,46,47,49,49,50,52,53,55,55],[56,57,59,61,62,64,65,65,66,67,68,68,69,70,71],[74,75,77,77,79,79,79,80,81,83,85,87,88,89,89],[91,93,94,96,97,98,99,99,100,100,102,104,105,107,107],[110,112,114,114,115,117,117,118,118,120,120,121,123,124,124],[127,127,129,131,133,134,134,135,137,139,139,140,142,143,144],[145,146,147,149,151,151,153,155,156,156,158,160,162,162,163]], 107)