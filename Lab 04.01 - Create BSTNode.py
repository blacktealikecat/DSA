class BSTNode:
    def __init__(self, data: int = None):
        
        self.data = data
        self.left = None
        self.right = None


data = int(input())
n = BSTNode(data)

print(n.data)
print(n.left)
print(n.right)