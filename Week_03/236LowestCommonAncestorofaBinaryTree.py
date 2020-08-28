# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root

        res = self.helper(root, p, q)
        return res

    def helper(self, node, p, q):
        if not node or node == p or node == q:
            return node

        left = self.helper(node.left, p, q)
        right = self.helper(node.right, p, q)

        if left and right:
            return node

        if left:
            return left

        if right:
            return right
