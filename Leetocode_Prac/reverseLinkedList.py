# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(head: ListNode) -> ListNode:

        if not head or not head.next:
            return head

        pre = head
        cur = head.next

        # dummy_head  ->  1  ->  2  ->  3  ->  4  ->  5->NULL
        # 1              pre <- cur   temp
        # 2                     pre <- cur    temp
        # F                                          cur
        if cur.next:
            temp = cur.next
            cur.next = pre
            pre.next = None

            cur = temp
            pre = cur

        while cur.next:
            temp = cur.next

            cur.next = pre

            cur = temp
            pre = cur

        return cur

        print(reverseList(node1))

node1=ListNode(1)
node2=ListNode(2)
node3=ListNode(3)
node4=ListNode(4)
node5=ListNode(5)

node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5








