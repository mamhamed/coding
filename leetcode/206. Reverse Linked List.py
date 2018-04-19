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
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        ptr_minus_1 = head
        ptr = head.next
        ptr_minus_1.next = None
        while ptr is not None and ptr.next is not None:
            ptr_plus_1 = ptr.next
            ptr.next = ptr_minus_1
            ptr_minus_1 = ptr
            ptr = ptr_plus_1

        ptr.next = ptr_minus_1

        return ptr

n1 = ListNode(1)
n2 = ListNode(2)
n1.next = n2
n3 = ListNode(3)
n2.next = n3
n4 = ListNode(4)
n3.next = n4
n5 = ListNode(5)
n4.next = n5

print n1
print Solution().reverseList(n1)

n1 = ListNode(1)
print n1
print Solution().reverseList(n1)

n1 = ListNode(1)
n2 = ListNode(2)
n1.next = n2
print n1
print Solution().reverseList(n1)
