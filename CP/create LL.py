class Node:
    def __init__ (self,val):
        self.val=val
        self.next=None
class LinkedList:
    def __init__ (self):
        self.head=None
    def create(self,n):
        i=0
        while i<n:
            new_node=Node(input("Enter value:"))
            if i==0:
                self.head=new_node
            else:
                t=self.head
                while t.next:
                    t=t.next
                t.next=new_node
            i=i+1
         def show(self):
             t=self.head
             while t:
                 print(t.val,end=",")
                 t=t.next

obj=LinkedList()
obj.createLL(n)
obj.show()

