# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import sys
class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return -1

        self.val = root.val
        self.smallest = sys.maxint
        self.traverse(root)
        if self.smallest == sys.maxint:
            return -1

        return self.smallest

    def traverse(self, root):
        if root is None:
            return

        if self.val < root.val < self.smallest:
            self.smallest = root.val

        self.traverse(root.left)
        self.traverse(root.right)


n1 = TreeNode(2)
n2 = TreeNode(2)
n3 = TreeNode(5)
n4 = TreeNode(5)
n5 = TreeNode(7)
n1.left = n2
n1.right = n3
n3.left = n4
n3.right = n5
print Solution().findSecondMinimumValue(n1)

n1 = TreeNode(5)
n2 = TreeNode(5)
n3 = TreeNode(6)
n1.left = n2
n1.right = n3
print Solution().findSecondMinimumValue(n1)

n1 = TreeNode(5)
n2 = TreeNode(8)
n3 = TreeNode(5)
n1.left = n2
n1.right = n3
print Solution().findSecondMinimumValue(n1)

n1 = TreeNode(2)
n2 = TreeNode(2)
n3 = TreeNode(2)
n1.left = n2
n1.right = n3
print Solution().findSecondMinimumValue(n1)


n1 = TreeNode(1)
n2 = TreeNode(3)
n3 = TreeNode(1)
n4 = TreeNode(2)
n5 = TreeNode(2)
n1.left = n2
n1.right = n3
n3.left = n4
n3.right = n5
print Solution().findSecondMinimumValue(n1)