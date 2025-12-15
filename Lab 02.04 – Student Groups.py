class ArrayStack:
    def __init__(self):
        self.size = 0
        self.data = list()
    
    def push(self, input_data):
        try:
            if input_data.isdigit():
                input_data = int(input_data)
            elif input_data.replace(".", "", 1).isdigit():
                input_data = float(input_data)
        except (TypeError, ValueError, ArithmeticError, AttributeError):
            pass
        finally:
            self.data.append(input_data)
            self.size += 1
    
    def pop(self):
        if self.size == 0:
            print("Underflow: Cannot pop data from an empty list")
            return None
        self.size -= 1
        return self.data.pop()
    
    def is_empty(self):
        if len(self.data) == 0 and self.size == 0:
            return True
        else:
            return False
    
    def get_stack_top(self):
        if self.is_empty():
            print("Underflow: Cannot get stack top from an empty list", end="")
            return None
        a = None
        for i in self.data:
            a = i
        return a
    
    def get_size(self):
        return self.size
    
    def print_stack(self):
        print(self.data)




m = int(input())
n = int(input())

stack = ArrayStack()
for i in range(n):
    name = input()
    stack.push(name)

all_groups = ArrayStack()
for i in range(m):
    all_groups.push(ArrayStack())

group_num = 0
while not stack.is_empty():
    student = stack.pop()
    
    temp_stack = ArrayStack()
    for j in range(m - group_num):
        temp_stack.push(all_groups.pop())
    
    now = temp_stack.pop()
    now.push(student)
    
    all_groups.push(now)
    while not temp_stack.is_empty():
        all_groups.push(temp_stack.pop())
    
    group_num = (group_num + 1) % m


result_stack = ArrayStack()
while not all_groups.is_empty():
    result_stack.push(all_groups.pop())


for i in range(1, m + 1):
    now = result_stack.pop()
    
    ans = f"Group {i}: "
    

    swap = ArrayStack()
    while not now.is_empty():
        swap.push(now.pop())
    
    first = True
    while not swap.is_empty():
        if not first:
            ans += ", "
        ans += swap.pop()
        first = False
    
    print(ans)