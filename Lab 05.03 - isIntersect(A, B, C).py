def isIntersect(a, b, c):
    return len(set(a) & set(b) & set(c)) > 0

a = input().split()
b = input().split()
c = input().split()

print(isIntersect(a, b, c))