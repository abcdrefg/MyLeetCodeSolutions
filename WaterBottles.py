class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        empty_bottles = 0
        drunk_bottles = 0

        while (empty_bottles + numBottles) >= numExchange:
            drunk_bottles += numBottles
            empty_bottles += numBottles
            numBottles = empty_bottles // numExchange
            empty_bottles = empty_bottles % numExchange
        drunk_bottles += numBottles
        return drunk_bottles

Solution().numWaterBottles(15, 4)