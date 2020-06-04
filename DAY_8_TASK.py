def inOrder(node, stack=[]):
    if node.left:
        inOrder(node.left, stack)
    stack.append(node.data)
    if node.right:
        inOrder(node.right, stack)

        
def is_bst_satisfied(self):
    stack = []
    inOrder(self.root, stack)
    length = len(stack)
    for i in range(length-1):
        if stack[i] >= stack[i+1]:
            return False
    return True