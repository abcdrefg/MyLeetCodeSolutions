class Solution:

    def set_left_pointer(s, t):
        left_pointer = 0
        size = len(s)
        while True:
            if (t[0] != s[left_pointer]):
                left_pointer += 1
                continue
            break
        return left_pointer

    def isSubsequence(self, t: str, s: str) -> bool:
        size = len(s)
        right_pointer = size - 1

        t_size = len(t)
        if t_size == 0:
            return True
        if size <= t_size:
            if s != t:
                return False

        t_left_pointer = 0
        t_right_pointer = t_size - 1

        left_pointer = 0  # set_left_pointer(s, t)

        while True:
            if s[left_pointer] != t[t_left_pointer]:
                left_pointer += 1
            else:
                t_left_pointer += 1
                left_pointer += 1

            if s[right_pointer] != t[t_right_pointer]:
                right_pointer -= 1
            else:
                t_right_pointer -= 1
                right_pointer -= 1

            if t_left_pointer > t_right_pointer:
                return True

            if left_pointer >= right_pointer:
                if t_left_pointer == t_right_pointer and left_pointer == right_pointer and s[left_pointer] == t[t_left_pointer]:
                    return True
                return False

print(Solution().isSubsequence("b", "abc"))