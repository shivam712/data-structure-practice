#TASK 1
class Node:
    def __init__(self,data,next_node=None):
        self.data=data
        self.next=next_node
    def get_value(self):
        return self.data
    def get_next_node(self):
        return self.next
    def set_next_node(self,next_node):
        self.next=next_node
# my_node=Node(44)
# print(my_node.get_value())

#TASK 2

class LinkedList():
    def __init__(self,value=None):
        self.head_node=value
    def get_head_node(self):
        return self.head_node
    def insert_beginning(self,new_value):
        new_node=Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node=new_node
    def stringify_list(self):
        self.string=""
        self.current=self.head_node
        while(self.current):
            self.string+=str(self.current.get_value())+"\n"
            self.current=self.current.next
        return self.string
    def remove_node(self,value_to_remove):
        self.current_node=self.head_node
        if self.head_node.get_value()==value_to_remove:
            self.head_node=self.head_node.get_next_node()
        else:
            while(self.current_node and self.current_node.get_next_node().get_value()!=value_to_remove):
                self.current_node=self.current_node.get_next_node()
            self.current_node.set_next_node(self.current_node.get_next_node().get_next_node())
    
#Final Task
ll=LinkedList()
ll.insert_beginning("A")
ll.insert_beginning("B")
ll.insert_beginning("C")
ll.insert_beginning("D")
print(ll.stringify_list())
ll.remove_node('D')
print(ll.stringify_list())
    