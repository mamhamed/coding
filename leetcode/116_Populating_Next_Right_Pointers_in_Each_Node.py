# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root is None:
            return None
        if root.left is not None:
            root.left.next = root.right
            if root.next is not None:
                root.right.next = root.next.left
            self.connect(root.left)
            self.connect(root.right)
        return;





t1 = TreeLinkNode(1)
t2 = TreeLinkNode(2)
t3 = TreeLinkNode(3)
t4 = TreeLinkNode(4)
t5 = TreeLinkNode(5)
t6 = TreeLinkNode(6)
t7 = TreeLinkNode(7)

t1.left = t2
t1.right = t3
t2.left = t4
t2.right = t5
t3.left = t6
t3.right = t7

Solution().connect(t1)