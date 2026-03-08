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


    def delete(self, data):
        self.deleted = None

        def dell(node, data):
            if node is None:
                return None

            if data < node.data: # ค่าที่จะลบอยู่ซ้าย
                node.left = dell(node.left, data)

            elif data > node.data: # ค่าที่จะลบอยู่ขวา
                node.right = dell(node.right, data)

            else:
                self.deleted = node.data

                # ไม่มีลูก
                if node.left is None and node.right is None:
                    return None

                # มีลูก 1 คน (ขวา)
                if node.left is None:
                    return node.right

                # มีลูก 1 คน (ซ้าย)
                if node.right is None:
                    return node.left

                # มีลูก 2 คน
                parent = node
                child = node.left

                while child.right is not None: # ตามหา Max ของ Subtree ซ้าย
                    parent = child
                    child = child.right

                node.data = child.data

                if parent == node:
                    parent.left = child.left
                else:
                    parent.right = child.left

            return node

        self.root = dell(self.root, data)

        if self.deleted is None:
            print("Delete Error, " + str(data) + " is not found in Binary Search Tree.")
            return None

        return self.deleted


    def find_min(self):
        if self.is_empty():
            return None

        here = self.root
        
        while here.left is not None:
            here = here.left

        return here.data


    def find_max(self):
        if self.is_empty():
            return None

        here = self.root
        
        while here.right is not None:
            here = here.right

        return here.data


    def is_empty(self):
        return self.root is None


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
  while 1:
    text = input()
    if text == "Done":
      break
    condition, data = text.split(": ")
    if condition == "I":
      my_bst.insert(int(data))
    elif condition == "D":
      my_bst.delete(int(data))
    else:
      print("Invalid Condition")
  my_bst.traverse()

main()