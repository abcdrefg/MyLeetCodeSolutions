class Solution:
    def isSymmetric(self, root) -> bool:

        def check_node_pairs(p, q):
            if not q and not p:
                return True

            if q and p:
                return q.val == p.val and check_node_pairs(p.left, q.right) and check_node_pairs(p.right, q.left)

            return False

        if not root.left and not root.right:
            return True
        if not root.left or not root.right:
            return False

        return check_node_pairs(root.left, root.right)