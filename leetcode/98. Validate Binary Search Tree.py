from tree_utils import *
import sys

class Solution(object):
    def isValidBST(self, root):
        _, _, isvalid = self.isValidBST2(root)
        return isvalid

    def isValidBST2(self, root):
        if root is None:
            return -sys.maxint, sys.maxint, True

        min_left, max_left, isvalid_left = self.isValidBST2(root.left)
        min_right, max_right, isvalid_right = self.isValidBST2(root.right)

        return min(min_right, min_left), max(max_left, max_right), root.val > max_left and root.val < min_right and isvalid_left and isvalid_right