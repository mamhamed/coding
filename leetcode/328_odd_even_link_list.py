# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        node = self
        mystr = str(self.val) + "\t"
        while node.next is not None:
            mystr += str(node.next.val) + "\t"
            node = node.next

        return mystr


class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head

        head_odd = odd = ListNode(0)
        head_even = even = ListNode(0)

        node = head
        while(node is not None):
            odd.next = node
            even.next = node.next

            if node.next is None:
                node = None
                odd = odd.next
            else:
                node = node.next.next
                odd = odd.next
                even = even.next

        odd.next = head_even.next

        return head_odd.next


node1 = ListNode(1)
node2 = ListNode(2)
node1.next = node2
node3 = ListNode(3)
node2.next = node3
# node4 = ListNode(4)
# node3.next = node4
# node5 = ListNode(5)
# node4.next = node5
# node6 = ListNode(6)
# node5.next = node6
# node7 = ListNode(7)
# node6.next = node7
# node8 = ListNode(8)
# node7.next = node8

a = Solution().oddEvenList(node1)
print node1