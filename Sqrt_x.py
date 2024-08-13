class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        if x == 0:
            return 0
        bottom = 1
        top = x
        while True:
            mid = (top + bottom) / 2
            result = mid*mid
            if (abs(result - x) < 0.01):
                if round(mid)*round(mid) == x:
                    return round(mid)
                return int(mid)
            if result > x:
                top = mid - 0.1
            elif result == x:
                return result
            else:
                bottom = mid + 0.1
        return round(mid)

Solution().mySqrt(1024)