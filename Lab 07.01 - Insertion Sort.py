def InsertionSort(list, last):
    
    count = 0
    
    for current in range(1, last + 1):
        hold = list[current]
        walker = current - 1
        
        while walker >= 0 and hold < list[walker]:
            count += 1
            list[walker + 1] = list[walker]
            walker -= 1
        
        if walker >= 0:
            count += 1
        
        list[walker + 1] = hold
        print(list)
    
    print(f"Comparison times: {count}")



import json
data_input = input()
last_index = int(input())
data_list = json.loads(data_input)
InsertionSort(data_list, last_index)
