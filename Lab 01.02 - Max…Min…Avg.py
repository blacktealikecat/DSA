import json

def main():
    mylist = json.loads(input())
    high = mylist[0]
    low = mylist[0]
    total = 0
    count = 0
    
    for i in mylist:
        if i > high:
            high = i
        if i < low:
            low = i
    
        total += i
        count += 1
        
    avg = total / count
    result = tuple((round(high, 2), round(low, 2), round(avg, 2)))
    return result

print(main())