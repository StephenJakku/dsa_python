from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        i = list1
        j = list2

        res = ListNode()
        print(res.val)
        while (i and j):
            if (i.val < j.val):
                print(i.val)
                print(res.val)
                res.val = i.val
                res = res.next
                i = i.next
            else:
                res.val = j.val
                res = res.next
                j = j.next
        return res




