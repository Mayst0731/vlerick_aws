class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None


l1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(4)
l1.next = node2
node2.next = node3


l2 = ListNode(1)
node5 = ListNode(3)
node6 = ListNode(4)
l2.next = node5
node5.next = node6

class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            if l2 is None:
                return None
            else:
                return l2
        if l2 is None:
            if l1 is None:
                return None
            else:
                return l1
        head1 = l1
        head2 = l2
        myNode = ListNode(0)
        current = myNode

        while head1 is not None and head2 is not None:
            if head1.val >= head2.val:
                current.next = head2
                head2 = head2.next
            else:
                current.next = head1
                head1 = head1.next
            current = current.next

        if (current.next == head1) and (head1 is not None):
            current.next = head1
        else:
            current.next = head2
            # current.next = p1 != None ? p1 : p2

        return myNode.next


testList = mergeTwoLists(l1, l2)
while testList is not None:
    print(myNode.val + '-->')
