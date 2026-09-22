# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if not subRoot:
            return True
        if root.val==subRoot.val:
            if self.isIdentical(root,subRoot):
                return True
        l=self.isSubtree(root.left,subRoot)
        r=self.isSubtree(root.right,subRoot)
        return l or r

    def isIdentical(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        if root.val!=subRoot.val:
            return False
        return self.isIdentical(root.left,subRoot.left) and self.isIdentical(root.right,subRoot.right)






















    #     if not subRoot:
    #         return True
    #     if not root:
    #         return False 
    #     if root.val==subRoot.val:
    #         if self.isIdentical(root,subRoot):
    #             return True
    #     l=self.isSubtree(root.left, subRoot)
    #     r=self.isSubtree(root.right, subRoot)
    #     return l or r


    # def isIdentical(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    #     if not root and not subRoot:
    #         return True
    #     if not root or not subRoot:
    #         return False
    #     if root.val!=subRoot.val:
    #         return False
    #     l=self.isIdentical(root.left, subRoot.left)
    #     r=self.isIdentical(root.right, subRoot.right)
    #     return l and r
    
        

        