# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        max_depth=0
        queue=deque([(root,1)])
        while queue:
            node,depth=queue.popleft()
            max_depth=max(max_depth,depth)
            if not node:
                return 0
            if node.left:
                queue.append((node.left,depth+1))
            if node.right:
                queue.append((node.right,depth+1))
        return max_depth







        # max_depth=0
        # if not root:
        #     return 0
        # def dfs(node,depth):
        #     nonlocal max_depth
        #     if not node:
        #         return 0
        #     dfs(node.left,depth+1)
        #     dfs(node.right,depth+1)
        #     max_depth=max(max_depth,depth)
        # dfs(root,1)
        # return max_depth





























    #     stack=[(root,1)]
    #     depth=0
    #     while stack:
    #         node,curr_sum=stack.pop()
    #         depth=max(depth,curr_sum)
    #         if not node:
    #             return 0
    #         if node.left:
    #             stack.append((node.left,curr_sum+1))
    #         if node.right:
    #             stack.append((node.right,curr_sum+1))
    #     return depth


    #     # if not root:
    #     #     return 0
    #     # leftDepth=self.maxDepth(root.left)
    #     # rightDepth=self.maxDepth(root.right)  
    #     # return 1+max(leftDepth,rightDepth)


        