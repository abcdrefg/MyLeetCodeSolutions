# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def searchForNodes(self, root, to_delete, is_root, parent, is_left):
        forest = []

        if root.val in to_delete:
            forest_left = []
            forest_right = []
            is_root = True
            if parent:
                if is_left:
                    parent.left = None
                else:
                    parent.right = None
            if root.left:
                forest_left = self.searchForNodes(root.left, to_delete, is_root, root, True)
            if root.right:
                forest_right = self.searchForNodes(root.right, to_delete, is_root, root, False)
            forest = forest + forest_left + forest_right
            return forest

        if is_root:
            forest.append(root)
            is_root = False

        forest_left = []
        forest_right = []
        if root.left:
            forest_left = self.searchForNodes(root.left, to_delete, is_root, root, True)
        if root.right:
            forest_right = self.searchForNodes(root.right, to_delete, is_root, root, False)
        forest = forest + forest_left + forest_right
        return forest

    def delNodes(self, root, to_delete):
        return self.searchForNodes(root, to_delete, True, None, False)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.right = TreeNode(4)


Solution().delNodes(root, [2, 1])

