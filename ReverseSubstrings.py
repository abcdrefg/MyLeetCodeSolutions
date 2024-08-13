class Solution:
    def reverseParentheses(self, s: str) -> str:
        starting_points = []
        ending_points = []
        for i in range(len(s)):
            if s[i] == '(':
                starting_points.append(i)
            elif s[i] == ')':
                ending_points.append(i)
        starting_points.reverse()

        created_string = s[starting_points[0]:ending_points[0]+1]
        created_string = created_string[::-1]

        if len(starting_points) == 1:
            if starting_points[len(starting_points) - 1] != 0:
                created_string = s[0:starting_points[len(starting_points) - 1]] + created_string
            if ending_points[len(ending_points) - 1] != len(s):
                created_string += s[ending_points[len(ending_points) - 1]:]
            created_string = created_string.replace('(', '')
            created_string = created_string.replace(')', '')
            return created_string

        for i in range(1, len(starting_points)):
            created_string = s[starting_points[i] : starting_points[i-1]] + created_string + s[ending_points[i-1] : ending_points[i]]
            created_string = created_string[::-1]

        if starting_points[len(starting_points) - 1] != 0:
            created_string = s[0:starting_points[len(starting_points) - 1]] + created_string
        if ending_points[len(ending_points) - 1] != len(s):
            created_string += s[ending_points[len(ending_points) - 1]:]

        created_string = created_string.replace('(', '')
        created_string = created_string.replace(')', '')
        return created_string

Solution().reverseParentheses("xs(xu)")