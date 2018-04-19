# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        mystr = str(self.val)
        root = self.next
        while root is not None:
            mystr += ' -> ' + str(root.val)
            root = root.next
        return mystr

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

        if node.next is None:
            return
        last_node = None
        while node is not None:
            if node.next is not None:
                node.val = node.next.val
                last_node = node
                node = node.next
            else:
                last_node.next = None
                node = last_node.next

# 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6
node1 = ListNode(1)
node2 = ListNode(2)
node1.next = node2
node3 = ListNode(6)
node2.next = node3
node4 = ListNode(3)
node3.next = node4
node5 = ListNode(4)
node4.next = node5
node6 = ListNode(5)
node5.next = node6
node6 = ListNode(6)
node5.next = node6
print node1
Solution().deleteNode(node6)
print node1