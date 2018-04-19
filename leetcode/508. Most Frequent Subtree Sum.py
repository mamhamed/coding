# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        _, arr = self.get_sum_of_subtree(root)
        dic = {}
        max_val = 0
        for i in arr:
            dic[i] = dic.get(i, 0) + 1
            if max_val < dic[i]:
                max_val = dic[i]

        res = []
        for i,v in dic.items():
            if v == max_val:
                res.append(i)

        return res

    def get_sum_of_subtree(self, root):
        if root is None:
            return 0, []
        if root.left is None and root.right is None:
            return root.val, [root.val]

        left, left_arr = self.get_sum_of_subtree(root.left)
        right, right_arr = self.get_sum_of_subtree(root.right)

        return root.val + left + right, [root.val + left + right] + left_arr + right_arr


node1 = TreeNode(5)
node2 = TreeNode(2)
node3 = TreeNode(-3)
node1.left = node2
node1.right = node3

print Solution().findFrequentTreeSum(node1)