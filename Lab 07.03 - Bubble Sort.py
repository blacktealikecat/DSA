def bubbleSort(lst: list, last: int):
    count = 0
    for current in range(last + 1):
        sorted = True
        for walker in range(last, current, -1):
            if lst[walker] < lst[walker - 1]:
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