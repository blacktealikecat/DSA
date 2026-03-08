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
        
    def insert_front(self, data):
        c = DataNode(data)
        
        c.next = self.head
        self.head = c
        
        self.count += 1

    def insert_before(self, node, data):
        if self.head is None:
            print("Cannot insert, " + node + " does not exist.")
            return
        
        
        if self.head.data == node:
            self.insert_front(data)
            return
        
        
        here = self.head
        
        while here.next is not None:
            
            if here.next.data == node:
                d = DataNode(data)
                d.next = here.next
                here.next = d
                
                self.count += 1
                return
            
            here = here.next
        
        # กรณีที่ไม่มีโหนดในลิสต์
        print("Cannot insert, " + node + " does not exist.")
        return

    def delete(self, data):
        if self.head is None:
            print("Cannot delete, " + data + " does not exist.")
            return
        
        
        # delete ตอนเป็น head เอง
        if self.head.data == data:
            self.head = self.head.next
            
            self.count -= 1
            return
        
        
        # reroll หาทีละตัว
        here2 = self.head
        while here2.next:
            if here2.next.data == data:
                here2.next = here2.next.next
                self.count -= 1
                return
            here2 = here2.next
        
        print("Cannot delete, " + data + " does not exist.")

# test
def main():
  mylist = SinglyLinkedList()
  for _ in range(int(input())):
    text = input()
    condition, data = text.split(": ")
    if condition == "F":
      mylist.insert_front(data)
    elif condition == "L":
      mylist.insert_last(data)
    elif condition == "B":
      mylist.insert_before(*data.split(", "))
    elif condition == "D":
      mylist.delete(data)
    else:
      print("Invalid Condition!")
  mylist.traverse()

main()