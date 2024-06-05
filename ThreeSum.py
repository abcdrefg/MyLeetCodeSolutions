class Solution:
    def threeSum(self, nums):
        size = len(nums)
        triples = []
        nums.sort()
        previous_point = None
        for i in range(size - 2):
            if previous_point == nums[i]:
                continue
            previous_point = nums[i]
            target = 0 - nums[i]
            left = i + 1
            right = size - 1
            while True:
                if left >= right:
                    break
                if nums[left] + nums[right] == target:
                    triples.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1]:
                        if left >= right:
                            break
                        left += 1
                if nums[left] + nums[right] > target:
                    right -= 1
                if nums[left] + nums[right] < target:
                    left += 1
        return triples

Solution().threeSum([0,0,0,0])