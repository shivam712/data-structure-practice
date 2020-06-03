def size_(self, node):
  if node is None:
            return 0
        return size_(node.left)+1+size_(node.right)
# write your code here
