class BSTNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None



class BST:
    def __init__(self):
        self.root = None


    def is_empty(self):
        return self.root is None


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


    def preorder(self, node=None):
        if node is None:
            node = self.root

        def pre(n):
            if n is None:
                return

            print("->", n.data, end=" ")
            pre(n.left)
            pre(n.right)

        pre(node)


    def inorder(self, node=None):
        if node is None:
            node = self.root

        def ln(n):
            if n is None:
                return
            
            ln(n.left)
            print("->", n.data, end=" ")
            ln(n.right)

        ln(node)


    def postorder(self, node=None):
        if node is None:
            node = self.root

        def post(n):
            if n is None:
                return
            post(n.left)
            post(n.right)
            print("->", n.data, end=" ")

        post(node)


    def traverse(self):
        if self.is_empty():
            print("This is an empty binary search tree.")
            return

        print("Preorder:", end=" ")
        self.preorder(self.root)
        print()

        print("Inorder:", end=" ")
        self.inorder(self.root)
        print()

        print("Postorder:", end=" ")
        self.postorder(self.root)
        print()





# test
def main():
  my_bst = BST()
  for i in range(int(input())):
    my_bst.insert(int(input()))
  my_bst.traverse()

main()