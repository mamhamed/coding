# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        mystr = ''
        if root is None:
            return ''

        queue = [root]
        while len(queue) > 0:
            node = queue.pop(0)
            if node is None:
                mystr += 'None' + ' '
            else:
                mystr += str(node.val) + ' '
                queue.append(node.left)
                queue.append(node.right)

        return mystr



    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == '' or data is None:
            return None

        values = data.split(' ')
        val = values.pop(0)
        root = TreeNode(val)
        parents = [root]
        while len(values) > 0 and len(parents) > 0:
            parent = parents.pop(0)
            for i in ('left', 'right'):
                val = values.pop(0)
                if val == 'None':
                    node = None
                else:
                    node = TreeNode(int(val))
                    parents.append(node)
                if i == 'left':
                    parent.left = node
                else:
                    parent.right = node

        return root





t1 = TreeNode(1)
t2 = TreeNode(2)
t1.left = t2
t3 = TreeNode(3)
t1.right = t3
t4 = TreeNode(4)
t3.left = t4
t5 = TreeNode(5)
t3.right = t5
t6 = TreeNode(6)
t4.right = t6
t7 = TreeNode(7)
t5.left = t7

d = Codec().serialize(t1)
print d
t_hat = Codec().deserialize(d)
t_hat