class Node:
    def __init__(self,value,link_node=None):
        self.value=value
        self.link_node=link_node

    def get_value(self):
        return self.value

    def get_link_node(self):
        return self.link_node

    def set_link_node(self,link_node):
        self.link_node=link_node

#Creating stack class
class Stack:
    def __init__(self):
        self.top_item=None
    def push(self,value):
        self.new_item=Node(value)
        self.new_item.set_link_node(self.top_item)
        self.top_item=self.new_item
    def pop(self):
        self.item_to_remove=self.top_item
        self.top_item=self.item_to_remove.get_link_node()
        return self.item_to_remove.get_value()
    def peek(self):
        return self.top_item.get_value()
s=Stack()
s.push(10)
s.push(20)
print("Top Item",s.peek())
s.push(30)
print("Popped",s.pop())
print("Top Item",s.peek())
s.push(40)
print("Top Item",s.peek())
s.push(50)
print("Top Item",s.peek())
print("Popped",s.pop())
print("Top Item",s.peek())
