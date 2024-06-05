class Solution:
    def simplifyPath(self, path: str) -> str:
        simplified_path = []
        size = len(path)
        current_dir = ''
        for i in range(1, size):
            if path[i] == '/':
                if current_dir == '.' or current_dir == '':
                    current_dir = ''
                    continue
                if current_dir == '..':
                    if simplified_path:
                        simplified_path.pop()
                    current_dir = ''
                    continue
                simplified_path.append(current_dir)
                current_dir = ''
                continue
            current_dir += path[i]
        if current_dir != '' and current_dir[0] != '.':
            simplified_path.append(current_dir)
        if current_dir == '..':
            simplified_path.pop()
        return "/" + "/".join(simplified_path)










print(Solution().simplifyPath("/a//b////c/d//././/.."))