import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        s = s.lower()
        size = len(s)
        if size < 2:
            return True
        left = 0
        right = size - 1
        for i in range(size):
            if s[left] != s[right]:
                return False
            left +=1
            right -=1
            if left >= right:
                return True

Solution().isPalindrome("A man, a plan, a canal: Panama")