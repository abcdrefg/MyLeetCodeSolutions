class Solution:
    def sortColors(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size_of_nums = len(nums)
        number_of_colors = {}
        number_of_colors[0] = 0
        number_of_colors[1] = 0
        number_of_colors[2] = 0
        for num in nums:
            number_of_colors[num] += 1

        for i in range(number_of_colors[0]):
            nums[i] = 0

        for i in range(number_of_colors[0], number_of_colors[0] + number_of_colors[1]):
            nums[i] = 1

        for i in range(number_of_colors[1] + number_of_colors[0], number_of_colors[2] + number_of_colors[1] + number_of_colors[0]):
            nums[i] = 2


Solution().sortColors([2,0,2,1,1,0])