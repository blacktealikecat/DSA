def insertionSort(lst, last):
    count = 0
    
    def seat_key(seat):
        letter = seat[0]
        number = int(seat[1:])
        return (letter, number)
    
    for current in range(1, last + 1):
        main = lst[current]
        walker = current - 1
        
        while walker >= 0 and seat_key(main) < seat_key(lst[walker]):
            count += 1
            lst[walker + 1] = lst[walker]
            walker -= 1
        
        if walker >= 0:
            count += 1
        
        lst[walker + 1] = main
        print(lst)
    
    print(f"Comparison times: {count}")



import json
data_input = input()
last_index = int(input())
data_list = json.loads(data_input)
insertionSort(data_list, last_index)