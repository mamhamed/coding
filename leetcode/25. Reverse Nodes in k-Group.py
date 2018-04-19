from link_list_uitls import *
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head

        # return self.reverse(head)
        a, b = self.reverse_recursive(head)
        return a

    def reverse(self, head):
        if not head:
            return
        curr_node = head
        next_node = head.next
        curr_node.next = None

        while curr_node and next_node:
            tmp = next_node.next
            next_node.next = curr_node
            curr_node = next_node
            next_node = tmp

        return curr_node

    def reverse_recursive(self, head):
        if not head or not head.next:
            return head, head

        root, tmp = self.reverse_recursive(head.next)
        if tmp:
            head.next = None
            tmp.next = head
        return root, head






# the following swap every k nodes
# class Solution(object):
#     def reverseKGroup(self, head, k):
#         """
#         :type head: ListNode
#         :type k: int
#         :rtype: ListNode
#         """
#         if not head:
#             return head
#
#         ptr = k-1
#         prev = None
#         root = head
#         while ptr > 0 and head:
#             ptr -= 1
#             prev = head
#             head = head.next
#
#         if ptr > 0 or not head:
#             return root
#
#         tmp = root.next
#         prev.next = None
#         root.next = self.reverseKGroup(head.next, k)
#         if k > 2:
#             head.next = tmp
#             prev.next = root
#         else:
#             head.next = root
#
#         return head



print Solution().reverseKGroup(array_to_link_list([1]), 2)
print Solution().reverseKGroup(array_to_link_list([1,2]), 2)
print Solution().reverseKGroup(array_to_link_list([1,2,3,4,5]), 2)
print Solution().reverseKGroup(array_to_link_list([1,2,3,4,5]), 3)
print Solution().reverseKGroup(array_to_link_list([1,2,3,4,5,6,7]), 3)