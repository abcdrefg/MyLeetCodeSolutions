class Solution:

    def connect(self, root: 'Node') -> 'Node':

        def set_next_node(current_level_nodes):
            new_list = []

            most_left_node = None

            for node in current_level_nodes:
                if node and not most_left_node:
                    most_left_node = node
                    new_list.append(node.left)
                    new_list.append(node.right)
                    continue
                if node:
                    most_left_node.next = node
                    most_left_node = node
                    new_list.append(node.left)
                    new_list.append(node.right)
            if not new_list:
                return

            set_next_node(new_list)

        if not root:
            return None

        set_next_node([root.left, root.right])
        return root