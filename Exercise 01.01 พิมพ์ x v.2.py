def test(n):
    if n <= 0:
        print("Please enter a positive number.")
    for i in range(1, 1+n):
        print("x" * i)

n = int(input())
test(n)