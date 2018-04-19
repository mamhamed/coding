from tree_utils import *
from link_list_uitls import *


class SolutionInorder():
    def to_tree(self, l):
        size = self.size(l)
        if size == 1:
            return TreeNode(l.val)

        self.root = l
        tree = self.traverse(0, size)
        return tree

    def traverse(self, start, end):
        if start > end or not self.root:
            return None

        m = (start+end)/2
        left = self.traverse(start, m-1)
        tree = TreeNode(self.root.val)
        self.root = self.root.next
        tree.left = left
        right = self.traverse(m+1, end)
        tree.right = right
        return tree

    def size(self, head):
        l = 0
        while head:
            l += 1
            head = head.next
        return l


class SolutionPreOrder():
    def to_tree(self, l):
        size = self.size(l)
        self.head = l
        tree = self.traverse(0, size)
        return tree

    def traverse(self, start, end):
        if start > end or not self.head:
            return

        node = TreeNode(self.head.val)
        self.head = self.head.next
        node.left = self.traverse(start, (start+end)/2-1)
        node.right = self.traverse((start+end)/2+1, end)
        return node

    def size(self, head):
        l = 0
        while head:
            l += 1
            head = head.next
        return l


# print SolutionInorder().to_tree(array_to_link_list([1,2,3,4,5,6]))

print SolutionPreOrder().to_tree(array_to_link_list([1,2,3,4,5,6,7]))