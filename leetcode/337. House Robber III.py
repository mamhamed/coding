import tree_utils

class Solution(object):
    def __init__(self):
        self.memo = {}

    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.dfs(root)

    def dfs(self, root):
        if root is None:
            return 0

        if root in self.memo:
            return self.memo[root]

        if root.left is None and root.right is None:
            self.memo[root] = root.val
            return root.val

        without_root = self.dfs(root.right) + self.dfs(root.left)

        with_root = 0
        if root.right is not None:
            with_root += self.dfs(root.right.left) + self.dfs(root.right.right)
        if root.left is not None:
            with_root += self.dfs(root.left.left) + self.dfs(root.left.right)

        self.memo[root] = max(without_root, with_root+root.val)
        return self.memo[root]


n1 = tree_utils.convert_arr_to_tree([3,2,3,None,3,None,1])
print Solution().dfs(n1)