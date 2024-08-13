class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:

        search_for = "ab" if x > y else "ba"

        stack = []
        counter = 0
        for i in range(len(s)):
            if stack and s[i] == search_for[1] and stack[-1] == search_for[0]:
                stack.pop()
                counter += 1
                continue
            stack.append(s[i])
        points = x*counter if search_for == "ab" else y*counter
        counter = 0
        search_for =  search_for[::-1]
        s = "".join(stack)
        stack = []
        for i in range(len(s)):
            if stack and s[i] == search_for[1] and stack[-1] == search_for[0]:
                stack.pop()
                counter += 1
                continue
            stack.append(s[i])
        points = (x*counter) + points if search_for == "ab" else (y*counter) + points
        return points

Solution().maximumGain("cdbcbbaaabab", 4, 5)