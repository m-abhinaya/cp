n=input("Enter n val:")
class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def createLL(self,n):
        for val in n:
            new_node=Node(val)
            if self.head==None:
                self.head=new_node
            else:
                t=self.head
                while t.next:
                    t=t.next
                t.next=new_node
    def show(self):
        t=self.head
        while t:
            print(t.val,end=",")
            t=t.next

obj=LinkedList()
obj.createLL(n)
obj.show()
