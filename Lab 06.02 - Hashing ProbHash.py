class Student:
    def __init__(self, std_id: int, name: str, gpa: float):
        self.std_id = std_id
        self.name = name
        self.gpa = gpa

    def get_std_id(self):
        return self.std_id
    
    def get_name(self):
        return self.name
    
    def get_gpa(self):
        return self.gpa
    
    def print_details(self):
        print(f"ID: {self.std_id}")
        print(f"Name: {self.name}")
        print(f"GPA: {self.gpa:.2f}")

class ProbHash:
    def __init__(self, size: int = 0):
        self.__size = size
        self.__hash_table = [None] * size

    def __hash(self, key: int):
        return key % self.__size

    def insert_data(self, student):
        idx = start = self.__hash(student.std_id)
        
        while self.__hash_table[idx] is not None:
            idx = (idx + 1) % self.__size
            if idx == start:
                print(f"The list is full. {student.std_id} could not be inserted.")
                return
        
        self.__hash_table[idx] = student
        print(f"Insert {student.std_id} at index {idx}")

    def search_data(self, std_id):
        idx = start = self.__hash(std_id)
        
        while self.__hash_table[idx] is not None:
            if self.__hash_table[idx].std_id == std_id:
                print(f"Found {std_id} at index {idx}")
                return self.__hash_table[idx]
            idx = (idx + 1) % self.__size
            if idx == start:
                break
        
        print(f"{std_id} does not exist.")
        return None


# test
def main():
    import json
    size = int(input())
    hashtable = ProbHash(size)
    while True:
        finish = input()
        if finish == "Done":
            break
        condition, data = finish.split(" = ")
        if condition == "I":
            std_in = json.loads(data)
            std = Student(std_in["ID"], std_in["Name"], std_in["GPA"])
            hashtable.insert_data(std)
        elif condition == "S":
            print("------")
            student = hashtable.search_data(int(data))
            if student is not None:
                student.print_details()
            print("------")
        else:
            print("Invalid Condition!")
main()