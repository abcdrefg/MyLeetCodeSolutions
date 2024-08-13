class Solution:
    def hIndex(self, citations) -> int:
        citations.sort()
        number_of_citations = len(citations)
        for i in range(number_of_citations):
            if citations[i] >= (number_of_citations - i - 1):
                return min(citations[i], (number_of_citations - i))
        return 0

Solution().hIndex([3,0,6,1,5])