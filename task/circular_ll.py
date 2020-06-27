class Node:  
  def __init__(self, data):  
        self.data = data
        self.next = None  
  
class LinkedList:  
    def __init__(self):  
        self.head = None

def isCircularList(head):
    if(head == None):
      return True
    node=head.next
    while (node != None) and (node != head):
        node = node.next
    if(node == head):
      return True
    return False

llist = LinkedList()  
llist.head = Node(1) 
second = Node(2) 
third = Node(3)  
fourth = Node(4) 
      
llist.head.next = second; 
second.next = third; 
third.next = fourth 
      
print(isCircularList(llist.head))

      
fourth.next = llist.head 
      
print(isCircularList(llist.head))