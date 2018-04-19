import sys
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.p1 = None
        self.p2 = None
        self.prev = TreeNode(-sys.maxint)
        self.traverse(root)
        self.p1.val, self.p2.val = self.p2.val, self.p1.val
        return

    def traverse(self, root):
        if root is None:
            return

        self.traverse(root.left)

        if self.p1 is None and root.val <= self.prev.val:
            self.p1 = self.prev

        if self.p1 is not None and root.val <= self.prev.val:
            self.p2 = root

        self.prev = root
        self.traverse(root.right)



# n1 = TreeNode(0)
# n2 = TreeNode(1)
# n1.left = n2
# Solution().recoverTree(n1)

n1 = TreeNode(2)
n2 = TreeNode(3)
n1.right = n2
n3 = TreeNode(1)
n2.left = n3
Solution().recoverTree(n1)


# n1 = TreeNode(4)
# n2 = TreeNode(5)
# n3 = TreeNode(3)
# # n2 = TreeNode(3)
# # n3 = TreeNode(5)
# n1.left = n3
# n1.right = n2
# n4 = TreeNode(3.5)
# n5 = TreeNode(2)
# n3.right = n4
# n3.left = n5
# n5 = TreeNode(6)
# n6 = TreeNode(4.5)
# n2.right = n5
# n2.left = n6
# Solution().recoverTree(n1)