# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        self.res=[]
        def dfs(curr):
            if not curr:
                return
            
            dfs(curr.left)
            self.res.append(curr.val)
            dfs(curr.right)
        dfs(root)
        self.res.sort()

        return self.res[k-1]

        