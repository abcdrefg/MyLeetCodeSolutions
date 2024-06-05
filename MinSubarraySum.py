class Solution:
    def minSubArrayLen(self, target: int, nums) -> int:
        current_sum = nums[0]
        window_start = 0
        window_end = 0
        size = len(nums)
        if current_sum >= target:
            return 1
        min_size = 0
        for i in range(1, size):
            if current_sum < target:
                window_end = i
                current_sum += nums[i]
            if current_sum >= target:
                current_size_of_subarray = window_end - window_start
                min_size = current_size_of_subarray + 1
                break
        while(True):
            while(True):
                if current_sum - nums[window_start] >= target and window_end > window_start:
                    min_size -= 1
                    current_sum -= nums[window_start]
                    window_start += 1
                else:
                    break
            if window_end == size - 1:
                break
            current_sum -= nums[window_start]
            current_sum += nums[window_end + 1]
            window_start += 1
            window_end += 1
        return min_size

Solution().minSubArrayLen(7, [2,3,1,2,4,3])