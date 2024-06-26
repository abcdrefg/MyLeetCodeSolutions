class Solution:
    def searchInsert(self, nums: [int], target: int) -> int:
        size_of_nums = len(nums)

        start_index = 0
        end_index = size_of_nums - 1

        while True:
            index = start_index + (end_index - start_index) // 2
            if nums[index] == target:
                return index
            elif nums[index] > target:
                end_index = index - 1
            else:
                start_index = index + 1
            if start_index > end_index:
                return start_index


Solution().searchInsert([1,3,5,6], 2)