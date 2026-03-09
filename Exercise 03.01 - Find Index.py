class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0


    def add(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node

        else:
            current = self.head
            while current.next is not None:
                current = current.next

            current.next = new_node
        self.size += 1


    def get(self, line):
        if line < 1 or line > self.size:
            return "Error"

        current = self.head

        for _ in range(line - 1):
            current = current.next

        return current.data




def main():
    ll = LinkedList()

    while True:
        line = input().strip()
        if line == "Last":
            break
        ll.add(line)

    line = int(input().strip())
    print(ll.get(line))

if __name__ == "__main__":
    main()