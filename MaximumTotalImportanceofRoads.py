from collections import Counter

class Solution:
    def maximumImportance(self, n: int, roads) -> int:
        connections_counter = [0] * n

        for road in roads:
            connections_counter[road[0]] += 1
            connections_counter[road[1]] += 1

        connections_counter.sort()
        sum_of_importance = 0
        iteration = 1
        for connections in connections_counter:
            sum_of_importance += connections * iteration
            iteration += 1
        return sum_of_importance

Solution().maximumImportance(5, [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]])