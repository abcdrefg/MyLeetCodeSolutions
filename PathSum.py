
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root, targetSum: int) -> bool:

        def check_sum(root, current_sum, target_sum):
            current_sum += root.val
            if current_sum == target_sum:
                return True
            if current_sum > target_sum:
                return False
            check_left_sub = False
            check_right_sub = False
            if root.left:
                check_left_sub = check_sum(root.left, current_sum, targetSum)
            if root.right:
                check_right_sub = check_sum(root.right, current_sum, targetSum)
            return (check_left_sub or check_right_sub)

        if not root:
            return False

        return check_sum(root, 0, targetSum)

root = TreeNode(5)
root.left = TreeNode(4)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)

Solution().hasPathSum(root, 22)