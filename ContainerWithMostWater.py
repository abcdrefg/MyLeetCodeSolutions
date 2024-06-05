class Solution:

    def calculateCap(self, right, left, length):
        if right >= left:
            return left*length
        return right*length

    def maxArea(self, height: [int]) -> int:
        left = 0
        right = len(height) - 1
        max_cap = self.calculateCap(height[right], height[left], right - left)
        while True:
            if right <= left:
                return max_cap
            cap = self.calculateCap(height[right], height[left], right - left)
            if cap > max_cap:
                max_cap = cap
            if height[left] >= height[right]:
                right -= 1
            else:
                left += 1

print(Solution().maxArea([2,3,4,5,18,17,6]))