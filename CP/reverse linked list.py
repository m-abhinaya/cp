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
    def show(self,head):
        t=head
        while t:
            print(t.val,end=",")
            t=t.next

    def reverseList(self,head):
        prev=None
        while head:
            cur=head
            head=head.next
            cur.next=prev
            prev=cur
        return prev
   
obj=LinkedList()
n=int(input("Enter n value"))
obj.createLL(n)
print("Linked List")
obj.show(obj.head)
print("\n after reverse:\n")
obj.head=obj.reverseList(obj.head)
obj.show(obj.head)

