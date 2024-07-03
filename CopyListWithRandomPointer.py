
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random



class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        root_copy = Node(head.val, None, None)
        head_root = head
        curr_node = root_copy
        index_to_node = {}
        index_to_node[0] = root_copy
        index_to_node[None] = None
        head = head.next
        i = 1
        while head != None:
            node = Node(head.val, None, None)
            curr_node.next = node
            curr_node = curr_node.next
            head = head.next
            index_to_node[i] = node
            i += 1
        head = head_root
        curr_node = root_copy
        while head != None:
            curr_node.random = index_to_node[head.random]
            curr_node = curr_node.next
            head = head.next
        return root_copy
