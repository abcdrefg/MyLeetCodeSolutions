class Solution:

    def calculateSize(self, max_window_size, window_start, window_end) -> int:
        window_size = window_end - window_start + 1
        if window_size > max_window_size:
            return window_size
        return max_window_size

    def lengthOfLongestSubstring(self, s: str) -> int:
        size_of_str = len(s)
        if size_of_str == 0:
            return 0
        window_start = 0
        window_end = 0
        max_window_size = 1
        letter_index = {}
        letter_index[s[0]] = 0
        for i in range(1, size_of_str):
            if s[i] not in letter_index:
                window_end = i
                letter_index[s[i]] = i
                max_window_size = window_end - window_start + 1
                continue
            if letter_index[s[i]] < window_start:
                window_end = i
                letter_index[s[i]] = i
                max_window_size = self.calculateSize(max_window_size, window_start, window_end)
                max_window_size = window_end - window_start + 1
                continue
            max_window_size = window_end - window_start + 1
            break
        while (True):
            if window_end + 1 > size_of_str - 1:
                break
            if s[window_end + 1] not in letter_index:
                window_end += 1
                letter_index[s[window_end]] = window_end
                max_window_size = self.calculateSize(max_window_size, window_start, window_end)
                continue
            if letter_index[s[window_end + 1]] < window_start:
                window_end += 1
                letter_index[s[window_end]] = window_end
                max_window_size = self.calculateSize(max_window_size, window_start, window_end)
                continue
            window_start += 1
        return max_window_size

Solution().lengthOfLongestSubstring("au")