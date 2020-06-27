from binarytree import tree
class Node(object):
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
    
class BinaryTree1(object):
  def __init__(self, root):
    self.root = Node(root)


tree1 = BinaryTree1(1)
tree1.root.left = Node(2)
tree1.root.right = Node(3)
tree1.root.left.left = Node(4)
tree1.root.left.right = Node(5)
tree1.root.right.left = Node(6)
tree1.root.right.right = Node(7)

tree1=tree()
print(tree1)