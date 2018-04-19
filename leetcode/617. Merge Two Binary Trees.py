# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 is None:
            return t2
        if t2 is None:
            return t1

        q1 = [t1]
        q2 = [t2]

        done = False
        while not done:
            q = zip(q1, q2)
            for a, b in q:
                if a is None and b is None:
                    continue
                elif a is None:
                    a = b
                elif b is None:
                    continue
                else:
                    a.val = a.val + b.val

            new_q1 = []
            for q in q1:
                if q is not None:
                    new_q1.append(q.left)
                    new_q1.append(q.right)
                else:
                    new_q1.append(None)
                    new_q1.append(None)
            new_q2 = []
            # todo make this a function
            for q in q2:
                if q is not None:
                    new_q2.append(q.left)
                    new_q2.append(q.right)
                else:
                    new_q2.append(None)
                    new_q2.append(None)

            done = not any(new_q1) and not any(new_q2)
            q1 = new_q1
            q2 = new_q2

        return t1

t11 = TreeNode(1)
t12 = TreeNode(2)
t13 = TreeNode(3)
t11.left = t13
t11.right = t12
t15 = TreeNode(5)
t13.left = t15

t21 = TreeNode(2)
t22 = TreeNode(1)
t23 = TreeNode(3)
t21.left = t22
t21.right = t23
t24 = TreeNode(4)
t21.right = t24
t25 = TreeNode(7)
t23.right = t25

# Solution().mergeTrees(t11, t21)


a = t11 and t11.left
a