# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:

        result = []
        _stack = collections.deque()

        curr_node = root
        while(curr_node or _stack):
            while(curr_node):
                _stack.append(curr_node)
                curr_node = curr_node.left

            curr_node = _stack.pop()
            result.append(curr_node.val)
            curr_node = curr_node.right
        return result
