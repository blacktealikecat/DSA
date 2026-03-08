class BSTNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None



class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = BSTNode(data)
            return

        here = self.root
        
        while True:
            if data < here.data:
                if here.left is None:
                    here.left = BSTNode(data)
                    return
                
                here = here.left
            else:
                if here.right is None:
                    here.right = BSTNode(data)
                    return
                
                here = here.right

    def preorder(self):
        def pre(node):
            if node is None:
                return
            
            print("->", node.data, end=" ")
            
            pre(node.left)
            pre(node.right)

        pre(self.root)






# test
def main():
  my_bst = BST()
  for i in range(int(input())):
    my_bst.insert(int(input()))
    
  print("Preorder: ", end="")
  my_bst.preorder()

main()