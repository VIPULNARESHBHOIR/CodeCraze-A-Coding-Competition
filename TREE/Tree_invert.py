class Node:
    def __init__(self,val=0, left=None, right=None):

        self.val= val
        self.left= left
        self.right= right


class Solution:
    def TreeInvert(self,root=None):

        if not root:
            return None
        
        rightVal = root.right
        root.right = root.left 
        root.left = rightVal

        self.TreeInvert(root.left)
        self.TreeInvert(root.right)

        return root

    
    def TreePrint(self,root):
        
        if not root:
            return
        else:
            print(root.val, end=",")

        self.TreePrint(root.left) 
        self.TreePrint(root.right)

        return "\n" 
    
#test case 1st

n1=Node(50)
n2=Node(20)
n3=Node(60)
n4=Node(5)
n5=Node(30)
n6=Node(45)
n7=Node(70)
n8=Node(65)
n9=Node(80)

n1.left= n2
n1.right= n3

n2.left= n4
n2.right= n5

n3.left= n6
n3.right= n7

n7.left=

print(Solution().TreePrint(n1))

head=Solution().TreeInvert(n1)

print(Solution().TreePrint(n1))




