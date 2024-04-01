class ListNode:
    def __init__(self,val,next=None):
        self.val=val
        self.next=None


class Solution:
    def isCYCLE(self, head=None) -> bool:
        if head == None:
            return False
        visited=set()
        while head != None:
            if head in visited:
                return True
            else:
                visited.add(head)
                head=head.next

        return False
        


# test case 2
l1= ListNode(1)
l2= ListNode(2)
l3= ListNode(3)

l1.next=l2
l2.next=l3
l3.next=l2

head=l1
print(Solution().isCYCLE(head))


