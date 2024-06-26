import math

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left_pointer = 0
        right_pointer = math.floor(math.sqrt(c))

        while left_pointer <= right_pointer:
            current_sum = left_pointer*left_pointer + right_pointer*right_pointer
            if current_sum > c:
                right_pointer -=1
                continue
            if current_sum < c:
                left_pointer += 1
                continue
            return True
        return False

Solution().judgeSquareSum(2)