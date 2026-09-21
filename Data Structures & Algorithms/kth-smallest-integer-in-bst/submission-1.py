# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # stack=[root]
        # values=[]
        # while stack:
        #     if not root:
        #         return None
        #     if root.left:
        #         stack.append(root.left)
        #     root=stack.pop()
        #     values.append(root.val)
        #     if root.right:
        #         stack.append(root.right)
        # return values[k-1]

        # arr=[]
        # def dfs(node):
        #     if not node:
        #         return 
            
        #     dfs(node.left)
        #     arr.append(node.val)
        #     dfs(node.right)
        # dfs(root)
        # #arr.sort()
        # return (arr[k-1])


        stack=[]
        node=root
        while True:
            while node:
                if not node:
                    return 
                stack.append(node)
                node=node.left
            node=stack.pop()
            k-=1
            if k==0:
                return node.val
            node=node.right


            
        
            
                
        