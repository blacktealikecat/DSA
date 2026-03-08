def SelectionSort(list, last):
    count = 0
    current = 0
    
    for current in range(0, last):
        smallest = current
        walker = current + 1
        
        while walker <= last:
            if list[walker] < list[smallest]:
                smallest = walker
            walker += 1
            count += 1
            
        list[current], list[smallest] = list[smallest], list[current]
        print(list)
    
    print(f"Comparison times: {count}")



import json
data_input = input()
last_index = int(input())
data_list = json.loads(data_input)
SelectionSort(data_list, last_index)