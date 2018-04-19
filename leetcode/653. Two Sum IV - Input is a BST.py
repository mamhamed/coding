# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if root is None:
            return False

        arr = []
        self.inorder(root, arr)

        ptr1 = 0
        ptr2 = len(arr)-1
        while ptr1 < ptr2:
            d = arr[ptr1] + arr[ptr2]
            if d == k:
                return True
            elif k > arr[ptr1] + arr[ptr2]:
                ptr1 += 1
            else:
                ptr2 -= 1

        return False

    def inorder(self, root, arr):
        if root is None:
            return

        self.inorder(root.left, arr)
        arr.append(root.val)
        self.inorder(root.right, arr)



# [0,-1,2,-3,null,null,4]
# -4
# [5,3,6,2,4,null,7]
# node1 = TreeNode(0)
# node2 = TreeNode(-1)
# node1.left = node2
# node3 = TreeNode(2)
# node1.right = node3
# node4 = TreeNode(-3)
# node2.left = node4
# node5 = TreeNode(4)
# node3.right = node4
# print Solution().findTarget(node1, -4)

node1 = TreeNode(2)
node2 = TreeNode(1)
node1.left = node2
node3 = TreeNode(3)
node1.right = node3
print Solution().findTarget(node1, 3)

## [1,0,4,-2,null,3], 7
node1 = TreeNode(1)
node2 = TreeNode(0)
node1.left = node2
node3 = TreeNode(4)
node1.right = node3
node4 = TreeNode(-2)
node2.left = node4
node5 = TreeNode(3)
node3.left = node5
print Solution().findTarget(node1, 7)