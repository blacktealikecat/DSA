def main(n):
    if n == 0:
        return 1
    else:
        # return 2 * main(n - 1) + 3
        return 2 ** (n + 2) - 3
n = int(input())
print(main(n))
