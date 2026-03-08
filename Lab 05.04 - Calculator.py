def calculator(n):
    if n == 1:
        print(1)
        
    else:
        d = len(str(n))
        
        total = n
        
        p = 1
        for i in range(1, d):
            total += 9 * p * i
            p *= 10
        
        total += (n - p + 1) * d
        return total

n = int(input())

print(calculator(n))