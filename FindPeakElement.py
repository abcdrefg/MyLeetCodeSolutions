class Solution:
    def findPeakElement(self, nums) -> int:
        nums_size = len(nums)
        if nums_size == 1:
            return 0
        if nums_size == 2:
            if nums[0] < nums[1]:
                return 1
            return 0
        low = 0
        high = nums_size - 1

        while low <= high:
            mid = low + (high - low) // 2
            if mid == nums_size - 1 or nums[mid] > nums[mid + 1]:
                if mid == 0 or nums[mid] > nums[mid - 1]:
                    return mid
                high = mid
                continue
            else:
                low = mid

Solution().findPeakElement([3,4,3,2,1])