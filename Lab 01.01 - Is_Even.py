def is_even(x):
    x = str(x)
    y = x[-1]
    if y in ["0", "2", "4", "6", "8"]:
        print("True")
    else:
        print("False")

x = int(input())
is_even(x)