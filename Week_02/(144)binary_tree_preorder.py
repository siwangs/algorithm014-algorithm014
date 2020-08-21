# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        return self.helper(root, result)

    def helper(self, node, result):

        if not node:
            return result

        result.append(node.val)
        result = self.helper(node.left, result)
        result = self.helper(node.right, result)

        return result
