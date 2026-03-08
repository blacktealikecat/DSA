def bubbleSort(lst: list, last: int):
    count = 0
    
    def seat_key(seat):
        letter = seat[0]
        number = int(seat[1:])
        return (letter, number)
    
    for current in range(last + 1):
        sorted = True
        for walker in range(last, current, -1):
            if seat_key(lst[walker]) < seat_key(lst[walker - 1]):
                sorted = False
                lst[walker], lst[walker - 1] = lst[walker - 1], lst[walker]
            count += 1
        print(lst)
        if sorted:
            break
    print(f"Comparison times: {count}")



import json
data_input = input()
last_index = int(input())
data_list = json.loads(data_input)
bubbleSort(data_list, last_index)