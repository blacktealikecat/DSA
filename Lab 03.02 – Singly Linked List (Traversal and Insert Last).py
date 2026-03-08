class DataNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def  __init__(self):
        self.count = 0
        self.head = None

    def traverse(self):
        if self.head is None:
            print("This is an empty list.")
            return
        a = self.head
        while a is not None:
            if a.next is not None:

                print(a.data+' -> ' ,end='')
            else:
                print(a.data)
            a = a.next
    
    def insert_last(self, data):
        b = DataNode(data)

        if self.head is None:
            self.head = b
        else:
            c = self.head

            while c.next is not None:
                c = c.next
            c.next = b

        self.count += 1

# test
def main():
    mylist = SinglyLinkedList()
    for _ in range(int(input())):
        mylist.insert_last(input())
    mylist.traverse()

main()