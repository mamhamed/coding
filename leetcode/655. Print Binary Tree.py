# Definition for a binary tree node.
import numpy as np
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """

        def depth(n):
            if n is None: return 0
            return max(depth(n.right), depth(n.left)) + 1

        h = depth(root)
        n = (1 << h) - 1
        res = [[""]*n for _ in range(h)]

        def put_val(node, height, bias=0):
            pos = ((1 << height)-1)/2
            res[h-height][bias+pos] = str(node.val)
            if node.left:
                put_val(node.left, height-1, bias)
            if node.right:
                put_val(node.right, height-1, bias=bias+pos+1)

        put_val(root, h)
        return res












# n1 = TreeNode(1)
# n2 = TreeNode(2)
# n1.left = n2
# d = Solution().printTree(n1)
# for a in d:
#     print a
# print "-------------------"
#
# n1 = TreeNode(1)
# n2 = TreeNode(2)
# n3 = TreeNode(3)
# n4 = TreeNode(4)
# n1.left = n2
# n1.right = n3
# n2.right = n4
# d = Solution().printTree(n1)
# for a in d:
#     print a
# print "-------------------"
#
# n1 = TreeNode(1)
# n2 = TreeNode(2)
# n3 = TreeNode(3)
# n4 = TreeNode(4)
# n5 = TreeNode(5)
# n1.left = n2
# n1.right = n5
# n2.left = n3
# n3.left = n4
# d = Solution().printTree(n1)
# for a in d:
#     print a
# print "-------------------"

n1 = TreeNode(3)
n2 = TreeNode(1)
n3 = TreeNode(5)
n1.left = n2
n1.right = n3
n4 = TreeNode(0)
n5 = TreeNode(2)
n2.left = n4
n2.right = n5
n6 = TreeNode(3)
n5.right = n6
n7 = TreeNode(4)
n8 = TreeNode(6)
n3.left = n7
n3.right = n8

d = Solution().printTree(n1)
for a in d:
    print a
print "-------------------"