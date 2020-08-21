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

          res, heap = [], []
           for i in range(len(nums)):
                heapq.heappush(heap, (-nums[i], i))
                if i + 1 >= k:
                    while heap and heap[0][1] < i + 1 - k:
                        heapq.heappop(heap)
                    res.append(-heap[0][0])
            return res
