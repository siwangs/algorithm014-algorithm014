# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        prehead = ListNode(-1)

        followingNode = prehead

        while l1 and l2:
            print(l1.val, l2.val)

            if l1.val <= l2.val:
                followingNode.next = l1
                l1 = l1.next
            else:
                followingNode.next = l2
                l2 = l2.next

            followingNode = followingNode.next

        followingNode.next = l1 if l1 else l2

        return prehead.next


a = [2, 3, 4, 5, 6, 7]
a[:m]
