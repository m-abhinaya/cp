class Node:
   def __init__(self,val):
      self.data = val
      self.next = None

class cyclicLinkedList:  
   def __init__(self):
      self.head = None
   def createLL(self,n):
       i=0
       while i<n:
           val=int(input("Enter values:"))
           new_node=Node(val)
           if self.head==None:
               self.head=new_node
           else:
               t=self.head
               while t.next != None:
                   t=t.next
               t.next=new_node
           i=i+1
   def showcycle(self):
        i=0
        curr=self.head
        while i<100:
            print(curr.val,end="-->")
            curr=curr.next
            i+=1

obj=cyclicLinkedList()
n=int(input("Enter n value"))
obj.createLL(n)
print("Linked List")
obj.show(obj.head)
