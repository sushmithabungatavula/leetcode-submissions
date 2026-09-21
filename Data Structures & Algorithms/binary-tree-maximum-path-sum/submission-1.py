# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path= float("-inf")
        def dfs(node):
            nonlocal max_path
            if not node:
                return 0
            left_path= max(0,dfs(node.left))
            right_path= max(0,dfs(node.right))

            path= node.val+left_path+right_path

            max_path=max(max_path,path)
            gain=node.val+max(left_path,right_path)
            return gain
        dfs(root)
        return max_path



    #     def dfs(node):
    #         nonlocal max_path
    #         if not node:
    #             return
    #         leftDown= self.getmax(node.left)
    #         rightDown=self.getmax(node.right)
    #         path=node.val + leftDown + rightDown
    #         max_path=max(max_path, path)
    #         dfs(node.left)
    #         dfs(node.right)
    #     dfs(root)
    #     return max_path

    # def getmax(self, root: Optional[TreeNode]) -> int:
    #     if not root:
    #         return 0
    #     left=self.getmax(root.left)
    #     right=self.getmax(root.right)
    #     path=root.val+max(left,right)
    #     return max(0, path)




