#display first odd nodes and next even nodes

class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def createLL(self,n):
        i=0
        while i<n:
            val=int(input("Enter data:"))
            new_node=Node(val)
            if self.head==None:
                self.head=new_node
            else:
                t=self.head
                while t.next != None:
                    t=t.next
                t.next=new_node
            i=i+1
    def rec_show(self,head):
        if head==None:
            return
        else:
            print(head.val,end=" ")
            self.rec_show(head.next)
            
    def oddEven(self,head):
        oddhead=self.head
        evenhead=self.head.next

        odd=oddhead
        even=evenhead

        while even and even.next:
            odd.next=even.next
            odd=odd.next
            even.next=odd.next
            even=even.next
        odd.next=evenhead
        self.rec_show(self.head)

obj=LinkedList()
obj.createLL(6)
obj.oddEven(obj.head)
    
            
