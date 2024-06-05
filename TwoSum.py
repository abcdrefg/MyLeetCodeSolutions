class Solution:
    def binary_search(self, arr, low, high, x):

        # Check base case
        if high >= low:

            mid = (high + low) // 2

            # If element is present at the middle itself
            if arr[mid] == x:
                return mid

            # If element is smaller than mid, then it can only
            # be present in left subarray
            elif arr[mid] > x:
                return self.binary_search(arr, low, mid - 1, x)

            # Else the element can only be present in right subarray
            else:
                return self.binary_search(arr, mid + 1, high, x)

        else:
            # Element is not present in the array
            return -1

    def twoSum(self, numbers, target: int):
        size = len(numbers)
        for i in range(size):
            index = self.binary_search(numbers, i + 1, size-1, target - numbers[i])
            if index > -1:
                return [i + 1, index + 1]

    def twoSumTwoPointers(self, numbers, target: int):
        left = 0
        right = len(numbers) - 1
        while True:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            if numbers[left] + numbers[right] > target:
                right -= 1
            if numbers[left] + numbers[right] < target:
                left += 1



print(Solution().twoSum([5,25,75], 100))
