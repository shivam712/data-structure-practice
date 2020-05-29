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

# What do we do if someone tries to peek() or pop() when our stack is empty?
# How do we keep someone from push()ing to a stack that has already reached its limit?


class Stack:
    def __init__(self,limit=1000):      #Set limit of Stack to 1000
        self.top_item=None
        self.limit=limit
        self.size=0

    def has_space(self):
        return self.limit>self.size
    
    def is_empty(self):
        return self.size==0

    def push(self,value):
        if self.has_space():
            self.new_item=Node(value)
            self.new_item.set_link_node(self.top_item)
            self.top_item=self.new_item
            self.size+=1
        else:
            print("Stack is Full!")

    def pop(self):
        if not self.is_empty():
            self.item_to_remove=self.top_item
            self.top_item=self.item_to_remove.get_link_node()
            self.size-=1
            return self.item_to_remove.get_value()
        else:
            print("Stack is Empty!")

    def peek(self):
        if not self.is_empty():
            return self.top_item.get_value()
        else:
            print("Stack is Empty!")
#Final Task
pizza_stack=Stack(5)
pizza_stack.pop()
pizza_stack.push('Neapolitan Pizza')
print('Peek:',pizza_stack.peek())
pizza_stack.push('Chicago Pizza')
pizza_stack.push('Sicilian Pizza')
print('Peek:',pizza_stack.peek())
pizza_stack.push('Greek Pizza')
print('Popped',pizza_stack.pop())
print('Peek:',pizza_stack.peek())
pizza_stack.push('California Pizza')
pizza_stack.push('Detroit Pizza')
print('Peek:',pizza_stack.peek())
pizza_stack.push('New York-Style Pizza')

""" 
Creating stack class
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

Operations
s=Stack()
s.push(10)
s.push(20)
print("Top Item",s.peek())          #Output: 20
s.push(30)
print("Top Item",s.peek())          #Output: 30
s.push(40)
print("Top Item",s.peek())          #Output: 40
s.push(50)
print("Top Item",s.peek())          #Output: 50
print("Popped",s.pop())             #Output: 50
print("Top Item",s.peek())          #Output: 40

""" 