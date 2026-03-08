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



def binary_search(data: list[Student], name):
    start, stop, count = 0, len(data) - 1, 0
    
    while start <= stop:
        count += 1
        mid = (start + stop) // 2
        
        if name > data[mid].name:
            start = mid + 1
        elif name < data[mid].name:
            stop = mid - 1
        else:
            print(f"Found {data[mid].name} at index {mid}")
            data[mid].print_details()
            print(f"Comparisons times: {count}")
            return
    
    print(f"{name} does not exists.\nComparisons times: {count}")



# test
import json
json_info_input = input()
who = input()
info_input = json.loads(json_info_input)
students = [Student(i["id"], i["name"], i["gpa"]) for i in info_input]

binary_search(students, who)