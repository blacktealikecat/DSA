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




def is_parentheses_matching(expression):
    stack = ArrayStack()
    err = False
    
    for char in expression:
        if char == '(':
            stack.push(char)
        elif char == ')':
            if stack.is_empty():
                err = True
                stack.pop()
            else:
                stack.pop()

    
    if stack.is_empty() and not err:
        print(f"Parentheses in {expression} are matched")
        return True
    else:
        print(f"Parentheses in {expression} are unmatched")
        return False
        
expression = input()
print(is_parentheses_matching(expression))