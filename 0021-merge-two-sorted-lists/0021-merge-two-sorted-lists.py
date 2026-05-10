# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if((not(list1)) and (not(list2))):  # 둘 다 빈 리스트인 경우
            return None
        elif((not(list1)) or (not(list2))): # 둘 중 하나만 빈 리스트인 경우
            return list1 or list2           # 값이 있는 리스트만 리턴
        else:
            head = tail = ListNode()        # tail, head는 같은 주소를 가리킴

            while(list1 and list2):         # 뛟우순다렙뷈릵
                if(list1.val < list2.val):
                    tail.next = list1
                    list1 = list1.next
                else:
                    tail.next = list2
                    list2 = list2.next
                tail = tail.next

            tail.next = list1 or list2

        return head.next