#hascycle
def hascycle(self):
    if self.head==None:
        return False
    slow=self.head
    fast=self.head.next
    while slow != Fast:
        slow=slow.next
        fast=fast.next.next
        if fast==None:
            return False
    return True
