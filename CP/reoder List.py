class Node:

	def __init__(self, d):
		self.data = d
		self.next = None
		
def list(node):
    if(node == None):
        return
    while(node != None):
        print(node.data," -> ", end = "")
        node = node.next

def reverselist(node):
	prev = None
	curr = node
	next=None
	while (curr != None):
		next = curr.next
		curr.next = prev
		prev = curr
		curr = next
	node = prev
	return node

def rearrange(node):

	slow = node
	fast = slow.next
	while (fast != None and fast.next != None):
		slow = slow.next
		fast = fast.next.next
	
	node1 = node
	node2 = slow.next
	slow.next = None
	
	node2 = reverselist(node2)
	
	node = Node(0) #Assign dummy Node
	
	curr = node
	
	while (node1 != None or node2 != None):
		
		if (node1 != None):
			curr.next = node1
			curr = curr.next
			node1 = node1.next
		
		if(node2 != None):
			curr.next = node2
			curr = curr.next
			node2 = node2.next
	
	node = node.next

head = None
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

list(head) 
rearrange(head) 
print()
list(head)
