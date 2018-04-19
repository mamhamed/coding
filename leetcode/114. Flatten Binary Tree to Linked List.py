from tree_utils import *
from link_list_uitls import *

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.ptr = None
        self.traverse(root)
        self.ptr

    def traverse(self, root):
        if root is None:
            return
        self.traverse(root.right)
        self.traverse(root.left)
        root.right = self.ptr
        root.left = None
        self.ptr = root

tree = convert_arr_to_tree([10,12,15,25,30,36,None])
print Solution().flatten(tree)