# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node,left,right):
            if not node:
                return True
            if not left<node.val<right:
                return False
            return dfs(node.left,left,node.val) and dfs(node.right,node.val,right)
        return dfs(root, float("-inf"), float("inf"))
            













    #     if not root:
    #         return True
    #     if root.left:
    #         if self.getmax(root.left)>=root.val:
    #             return False
    #     if root.right:
    #         if self.getmin(root.right)<=root.val:
    #             return False
    #     return self.isValidBST(root.left) and self.isValidBST(root.right)
        
    # def getmax(self,node):
    #     if not node:
    #         return float("-inf")
    #     return max(node.val, self.getmax(node.left), self.getmax(node.right))
    # def getmin(self,node):
    #     if not node:
    #         return float("inf")
    #     return min(node.val, self.getmin(node.left), self.getmin(node.right))
        