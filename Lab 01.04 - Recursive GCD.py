def gcd(a, b):
    if a == b:
        print(a)
    elif a == 0:
        print(b)
    elif b == 0:
        print(a)
    else:
        return gcd(b, a%b)

a = int(input())
b = int(input())
gcd(a, b)